from copy import deepcopy
import types
import json
from typing import List, Tuple
from lagent.schema import ActionReturn, ActionStatusCode, AgentReturn

from mmengine.registry import Registry

REGISTRY = Registry('helper')

try:
    import lagent
    import agentlego
except ImportError:
    lagent = None
    agentlego = None

class DummyTool(agentlego.tools.BaseTool):

    def __init__(self, toolmeta):
        self.toolmeta = agentlego.schema.ToolMeta.from_json_dict(toolmeta)
        self.set_parser(agentlego.parsers.DefaultParser)
        self._is_setup = False

    def apply(self, *args, **kwargs):
        return 'Dummy Result'

def dummy_action_executor(tools):
    return lagent.ActionExecutor(
        actions=[DummyTool(cfg).to_lagent() for cfg in tools])


def model_adapter(model):
    """Modify the generate method to accept and return single item."""
    if getattr(model, '_generate_is_wrapped', False):
        # Avoid wrap twice.
        return model

    from opencompass.utils import PromptList

    def chat(self, inputs, *args, **kwargs):
        prompt = PromptList()
        for item in inputs:
            msg = {'prompt': item['content']}
            if item['role'] == 'user':
                msg['role'] = 'HUMAN'
            elif item['role'] == 'assistant':
                msg['role'] = 'BOT'
            elif item['role'] == 'system':
                msg['role'] = 'SYSTEM'
            prompt.append(msg)
        return self.generate([prompt], *args, **kwargs)[0]

    model.chat = types.MethodType(chat, model)
    setattr(model, '_generate_is_wrapped', True)
    return model


def react_style_history(history, files, protocol) -> List[dict]:
    from lagent.schema import ActionReturn
    inner_steps = []
    if files:
        prompt = 'The related files are at ' + ', '.join(f'`{file["path"]}`'
                                                         for file in files)
        inner_steps.append(dict(role='system', content=prompt))
    for step in history:
        if step['role'] == 'user':
            inner_steps.append(dict(role='user', content=step['content']))
        elif step['role'] == 'assistant' and step.get('tool_calls'):
            name = step['tool_calls'][0]['function']['name']
            args = step['tool_calls'][0]['function']['arguments']
            response = "{action}{name}\n{action_input}{args}".format(
                action=protocol.action['begin'],
                name=name,
                action_input=protocol.action_input['begin'],
                args=json.dumps(args),
            )
            inner_steps.append(dict(role='assistant', content=response))
        elif step['role'] == 'tool' and step.get('content'):
            # action= ActionReturn(result=[dict(type='text', content=step['content'])])
            action= ActionReturn(result=[step['content']])
            inner_steps.append(dict(role='system', content=action.format_result()))
        elif step['role'] == 'assistant' and step.get('content'):
            inner_steps.append(dict(role='assistant', content=step['content']))
    return inner_steps


class LagentAgent:
    """Agent wrapper for Lagent.

    https://github.com/InternLM/lagent.
    """
    is_api = True

    def __init__(self,
                 agent_type,
                 llm,
                 actions=None,
                 tool_server=None,
                 tool_meta=None,
                 protocol=None,
                 **kwargs):
        llm = model_adapter(REGISTRY.build(llm))
        agent_cfg = {'type': agent_type, 'llm': llm, **kwargs}

        tools = {}
        if actions is not None:
            for action in actions:
                action = REGISTRY.build(action)
                if isinstance(action, agentlego.tools.BaseTool):
                    action = action.to_lagent()
                tools[action.name] = action
        if tool_server is not None:
            from agentlego.tools.remote import RemoteTool
            for tool in RemoteTool.from_server(tool_server):
                tools[tool.name] = tool.to_lagent()
        if tool_meta is not None:
            with open(tool_meta, 'r') as f:
                metas = json.load(f)
            for meta in metas.values():
                tool = DummyTool(meta).to_lagent()
                tools.setdefault(tool.name, tool)

        self.tools = tools

        if protocol is not None:
            protocol = REGISTRY.build(protocol)
            agent_cfg['protocol'] = protocol

        from lagent import BaseAgent, ActionExecutor
        agent_cfg['action_executor'] = ActionExecutor(tools.values())
        self.agent: BaseAgent = REGISTRY.build(agent_cfg)

    def reset(self):
        pass

    def gt_response(self, prompt):
        if 'CIReAct' in str(self.agent.__class__):
            gold = prompt
            prompt = f"""{self.agent._protocol.action['begin']} IPythonInterpreter
{self.agent._protocol.action_input['begin']} ```python\n{gold}\n```\n"""  # noqa
            action_input = dict(
                command=f"""```python\n{gold}\n```\n""",
                timeout=120,
            )
            response = self.agent._action_executor('IPythonInterpreter',
                                                   action_input)
            gt_response = dict(role='assistant', content=prompt)
            system_response = dict(
                role='system',
                content=self.agent._protocol.format_response(response))
            return [gt_response, system_response]
        else:
            gt_response = dict(role='assistant', content=prompt)
            return [gt_response]

    @property
    def template_parser(self):
        return self.agent._llm.template_parser

    @template_parser.setter
    def template_parser(self, value):
        self.agent._llm.template_parser = value

    def next_step(self, history, resources=None, stop=False):
        from lagent.schema import ActionReturn
        tools = []
        files = []
        if resources is not None:
            tools = [
                self.tools[item['name']] for item in resources
                if item['type'] == 'tool'
            ]
            files = [item for item in resources if item['type'] == 'file']

        action_executor = lagent.ActionExecutor(actions=tools)
        if stop:
            history = history + [{'role': 'user', 'content': 'Please summarize the chat history and give a final answer. Do not call any tools.'}]
        history = react_style_history(history, files, self.agent._protocol)
        prompt = self.agent._protocol.format(chat_history=[],
                                             inner_step=history,
                                             action_executor=action_executor)
        response = self.agent._llm.chat(prompt)
        thought, action_name, action_input = self.agent._protocol.parse(
            response, action_executor)
        # action: ActionReturn = action_executor(action_name, action_input)
        try:
            action: ActionReturn = action_executor(action_name, action_input)
        except Exception as e:
            action = ActionReturn(type=action_name, args=dict(text=action_input))
            action.state = ActionStatusCode.API_ERROR
            action.errmsg = str(e)
        if action.errmsg != None:
            if '当前分组上游负载已饱和' in action.errmsg:
                raise NotImplementedError("当前分组上游负载已饱和，请稍后再试")
            if '504 Gateway Time-out' in action.errmsg:
                raise NotImplementedError("504 Gateway Time-out，请稍后再试")

        if action.type == action_executor.finish_action.name:
            return dict(role='assistant', content=action.format_result())
        else:
            msg = {'role': 'assistant'}
            args = action.args
            if action.errmsg is not None:
                msg['error'] = dict(type=action.state.name, msg=action.errmsg)
                # Handle fallback args
                args = args.get('inputs', args)
            function = dict(name=action.type, arguments=args)
            msg['tool_calls'] = [dict(type='function', function=function)]
            return msg

    def chat(self, query, memory=None, resources=None):
        tools = []
        files = []
        if resources is not None:
            tools = {
                item['name']: self.tools[item['name']]
                for item in resources if item['type'] == 'tool'
            }
            """
tools: 
{
    'OCR': 
    {
        'name': 'OCR', 
        'description': 'This tool can recognize all text on the input image.', 
        'parameters': 
        [
            {
                'name': 'image', 
                'description': None, 
                'type': 'STRING'
            }, 
            {
                'name': 'lang', 
                'description': None, 
                'type': 'STRING'
            }
        ], 
        'required': ['image', 'lang'], 
        'parameter_description': 'If you call this tool, you must pass arguments in the JSON format {key: value}, where the key is the parameter name.'
    },
    ... # 包含当前vqa提供给agent的工具集合，不是所有工具的集合 
}
            """
            files = [item for item in resources if item['type'] == 'file']
            """
file: 
[
    {
        'type': 'file', 
        'filetype': 'image', 
        'path': '/network_space/server126/shared/yinshaofeng/ToolLLM/GTA/opencompass/data/gta_dataset/image/image_1.jpg'
    }, 
    {
        'type': 'file', 
        'filetype': 'image', 
        'path': '/network_space/server126/shared/yinshaofeng/ToolLLM/GTA/opencompass/data/gta_dataset/image/image_2.jpg'
    }
]
            """

        action_executor = self.agent._action_executor
        action_executor.actions = tools
        if memory is None:
            memory = []
            if files:
                prompt = 'The related files are at ' + ', '.join(
                    f'`{file["path"]}`' for file in files)
                memory.append(dict(role='user', content=prompt))
        memory.append(dict(role='user', content=query)) # memory: [{'role': 'user', 'content': 'The related files are at `/network_space/server126/shared/yinshaofeng/ToolLLM/GTA/opencompass/data/gta_dataset/image/image_1.jpg`, `/network_space/server126/shared/yinshaofeng/ToolLLM/GTA/opencompass/data/gta_dataset/image/image_2.jpg`'}, {'role': 'user', 'content': 'How much should I pay for the beer on the table according to the price on the menu?'}]

        agent_return = self.agent.chat(memory) # self.agent: <lagent.agents.react.ReAct object at 0x7ca962e38b50>

        steps = []
        for action in agent_return.actions:
            if action.type == action_executor.finish_action.name:
                step = dict(role='assistant', content=action.format_result())
                steps.append(step)
            else:
                step = {'role': 'assistant'}
                args = action.args
                if action.errmsg is not None:
                    step['error'] = dict(type=action.state.name,
                                         msg=action.errmsg)
                    # Handle fallback args
                    args = args.get('inputs', args)
                function = dict(name=action.type, arguments=args)
                step['tool_calls'] = [dict(type='function', function=function)]
                steps.append(step)
                steps.append(dict(role='tool', content=action.result))
        # steps: [{'role': 'assistant', 'content': " To find the price of the beer on the table, you would need to consult the menu or ask someone who has access to it. The file paths provided don't contain pricing information."}]
        # memory跟上面一样
        return steps, memory


class LagentAgentVisual:
    """Agent wrapper for Lagent.

    https://github.com/InternLM/lagent.
    """
    is_api = True

    def __init__(self,
                 agent_type,
                 llm,
                 actions=None,
                 tool_server=None,
                 tool_meta=None,
                 protocol=None,
                 **kwargs):
        llm = model_adapter(REGISTRY.build(llm))
        agent_cfg = {'type': agent_type, 'llm': llm, **kwargs}

        tools = {}
        if actions is not None:
            for action in actions:
                action = REGISTRY.build(action)
                if isinstance(action, agentlego.tools.BaseTool):
                    action = action.to_lagent()
                tools[action.name] = action
        if tool_server is not None:
            from agentlego.tools.remote import RemoteTool
            for tool in RemoteTool.from_server(tool_server):
                tools[tool.name] = tool.to_lagent()
        if tool_meta is not None:
            with open(tool_meta, 'r') as f:
                metas = json.load(f)
            for meta in metas.values():
                tool = DummyTool(meta).to_lagent()
                tools.setdefault(tool.name, tool)

        self.tools = tools

        if protocol is not None:
            protocol = REGISTRY.build(protocol)
            agent_cfg['protocol'] = protocol

        from lagent import BaseAgent, ActionExecutor
        agent_cfg['action_executor'] = ActionExecutor(tools.values())
        self.agent: BaseAgent = REGISTRY.build(agent_cfg)

    def reset(self):
        pass

    def gt_response(self, prompt):
        if 'CIReAct' in str(self.agent.__class__):
            gold = prompt
            prompt = f"""{self.agent._protocol.action['begin']} IPythonInterpreter
{self.agent._protocol.action_input['begin']} ```python\n{gold}\n```\n"""  # noqa
            action_input = dict(
                command=f"""```python\n{gold}\n```\n""",
                timeout=120,
            )
            response = self.agent._action_executor('IPythonInterpreter',
                                                   action_input)
            gt_response = dict(role='assistant', content=prompt)
            system_response = dict(
                role='system',
                content=self.agent._protocol.format_response(response))
            return [gt_response, system_response]
        else:
            gt_response = dict(role='assistant', content=prompt)
            return [gt_response]

    @property
    def template_parser(self):
        return self.agent._llm.template_parser

    @template_parser.setter
    def template_parser(self, value):
        self.agent._llm.template_parser = value

    def next_step(self, history, resources=None, stop=False):
        from lagent.schema import ActionReturn
        tools = []
        files = []
        if resources is not None:
            tools = [
                self.tools[item['name']] for item in resources
                if item['type'] == 'tool'
            ]
            files = [item for item in resources if item['type'] == 'file']

        action_executor = lagent.ActionExecutor(actions=tools)
        if stop:
            history = history + [{'role': 'user', 'content': 'Please summarize the chat history and give a final answer. Do not call any tools.'}]
        history = react_style_history(history, files, self.agent._protocol)
        prompt = self.agent._protocol.format(chat_history=[],
                                             inner_step=history,
                                             action_executor=action_executor)
        
        query_image_path = None
        for file in files:
            query_image_path = file['path']
        # if query_image_path end with 'png', type = png, else type = jpeg
        if query_image_path.endswith('png'):
            query_image_type = 'png'
        else:
            query_image_type = 'jpeg'

        from PIL import Image
        from io import BytesIO
        import base64
        with Image.open(query_image_path) as img:
            img.thumbnail((800, 800))
            if img.mode == 'P' or img.mode == 'RGBA':
                img = img.convert('RGB')
            buffered = BytesIO()
            img.save(buffered, format=query_image_type) 
            query_image = base64.b64encode(buffered.getvalue()).decode("utf-8")
        
        prompt[-1] = {
            'role': 'user',
            'content': [
                {"type": "text", "text": prompt[-1]['content']},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/{query_image_type};base64," + query_image,
                    }
                },
            ]
        }
        response = self.agent._llm.chat(prompt)
        thought, action_name, action_input = self.agent._protocol.parse(
            response, action_executor)
        try:
            action: ActionReturn = action_executor(action_name, action_input)
        except Exception as e:
            action = ActionReturn(
                type=action_name, args=dict(text=action_input))
            action.state = ActionStatusCode.API_ERROR
            action.errmsg = str(e)

        if action.type == action_executor.finish_action.name:
            return dict(role='assistant', content=action.format_result())
        else:
            msg = {'role': 'assistant'}
            args = action.args
            if action.errmsg is not None:
                msg['error'] = dict(type=action.state.name, msg=action.errmsg)
                # Handle fallback args
                args = args.get('inputs', args)
            function = dict(name=action.type, arguments=args)
            msg['tool_calls'] = [dict(type='function', function=function)]
            return msg

    def chat(self, query, memory=None, resources=None):
        tools = []
        files = []
        if resources is not None:
            tools = {
                item['name']: self.tools[item['name']]
                for item in resources if item['type'] == 'tool'
            }
            files = [item for item in resources if item['type'] == 'file']

        action_executor = self.agent._action_executor
        action_executor.actions = tools
        if memory is None:
            memory = []
            if files:
                prompt = 'The related files are at ' + ', '.join(
                    f'`{file["path"]}`' for file in files)
                memory.append(dict(role='user', content=prompt))

        # load image (only support single image now)
        query_image_path = None
        for file in files:
            query_image_path = file['path']
        # if query_image_path end with 'png', type = png, else type = jpeg
        if query_image_path.endswith('png'):
            query_image_type = 'png'
        else:
            query_image_type = 'jpeg'

        from PIL import Image
        from io import BytesIO
        import base64
        with Image.open(query_image_path) as img:
            img.thumbnail((800, 800))
            if img.mode == 'P' or img.mode == 'RGBA':
                img = img.convert('RGB')
            buffered = BytesIO()
            img.save(buffered, format=query_image_type) 
            query_image = base64.b64encode(buffered.getvalue()).decode("utf-8")

        query_content = [
            {"type": "text", "text": query},
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/{query_image_type};base64," + query_image,
                }
            },
        ]
        memory.append(dict(role='user', content=query_content)) 
        agent_return = self.agent.chat(memory)

        steps = []
        for action in agent_return.actions:
            if action.type == action_executor.finish_action.name:
                step = dict(role='assistant', content=action.format_result())
                steps.append(step)
            else:
                step = {'role': 'assistant'}
                args = action.args
                if action.errmsg is not None:
                    step['error'] = dict(type=action.state.name,
                                         msg=action.errmsg)
                    # Handle fallback args
                    args = args.get('inputs', args)
                function = dict(name=action.type, arguments=args)
                step['tool_calls'] = [dict(type='function', function=function)]
                steps.append(step)
                steps.append(dict(role='tool', content=action.result))
        return steps, memory
    
class LagentAgentVisualLocal:
    """Agent wrapper for Lagent.

    https://github.com/InternLM/lagent.
    """
    is_api = True

    def __init__(self,
                 agent_type,
                 llm,
                 actions=None,
                 tool_server=None,
                 tool_meta=None,
                 protocol=None,
                 **kwargs):
        llm = model_adapter(REGISTRY.build(llm))
        agent_cfg = {'type': agent_type, 'llm': llm, **kwargs}

        tools = {}
        if actions is not None:
            for action in actions:
                action = REGISTRY.build(action)
                if isinstance(action, agentlego.tools.BaseTool):
                    action = action.to_lagent()
                tools[action.name] = action
        if tool_server is not None:
            from agentlego.tools.remote import RemoteTool
            for tool in RemoteTool.from_server(tool_server):
                tools[tool.name] = tool.to_lagent()
        if tool_meta is not None:
            with open(tool_meta, 'r') as f:
                metas = json.load(f)
            for meta in metas.values():
                tool = DummyTool(meta).to_lagent()
                tools.setdefault(tool.name, tool)

        self.tools = tools

        if protocol is not None:
            protocol = REGISTRY.build(protocol)
            agent_cfg['protocol'] = protocol

        from lagent import BaseAgent, ActionExecutor
        agent_cfg['action_executor'] = ActionExecutor(tools.values())
        self.agent: BaseAgent = REGISTRY.build(agent_cfg)

    def reset(self):
        pass

    def gt_response(self, prompt):
        if 'CIReAct' in str(self.agent.__class__):
            gold = prompt
            prompt = f"""{self.agent._protocol.action['begin']} IPythonInterpreter
{self.agent._protocol.action_input['begin']} ```python\n{gold}\n```\n"""  # noqa
            action_input = dict(
                command=f"""```python\n{gold}\n```\n""",
                timeout=120,
            )
            response = self.agent._action_executor('IPythonInterpreter',
                                                   action_input)
            gt_response = dict(role='assistant', content=prompt)
            system_response = dict(
                role='system',
                content=self.agent._protocol.format_response(response))
            return [gt_response, system_response]
        else:
            gt_response = dict(role='assistant', content=prompt)
            return [gt_response]

    @property
    def template_parser(self):
        return self.agent._llm.template_parser

    @template_parser.setter
    def template_parser(self, value):
        self.agent._llm.template_parser = value

    def next_step(self, history, resources=None, stop=False):
        from lagent.schema import ActionReturn
        tools = []
        files = []
        if resources is not None:
            tools = [
                self.tools[item['name']] for item in resources
                if item['type'] == 'tool'
            ]
            files = [item for item in resources if item['type'] == 'file']

        action_executor = lagent.ActionExecutor(actions=tools)
        if stop:
            history = history + [{'role': 'user', 'content': 'Please summarize the chat history and give a final answer. Do not call any tools.'}]
        history = react_style_history(history, files, self.agent._protocol)
        prompt = self.agent._protocol.format(chat_history=[],
                                             inner_step=history,
                                             action_executor=action_executor)
        response = self.agent._llm.chat(prompt)
        thought, action_name, action_input = self.agent._protocol.parse(
            response, action_executor)
        action: ActionReturn = action_executor(action_name, action_input)

        if action.type == action_executor.finish_action.name:
            return dict(role='assistant', content=action.format_result())
        else:
            msg = {'role': 'assistant'}
            args = action.args
            if action.errmsg is not None:
                msg['error'] = dict(type=action.state.name, msg=action.errmsg)
                # Handle fallback args
                args = args.get('inputs', args)
            function = dict(name=action.type, arguments=args)
            msg['tool_calls'] = [dict(type='function', function=function)]
            return msg

    def chat(self, query, memory=None, resources=None):
        tools = []
        files = []
        if resources is not None:
            tools = {
                item['name']: self.tools[item['name']]
                for item in resources if item['type'] == 'tool'
            }
            files = [item for item in resources if item['type'] == 'file']

        action_executor = self.agent._action_executor
        action_executor.actions = tools
        if memory is None:
            memory = []
            if files:
                prompt = 'The related files are at ' + ', '.join(
                    f'`{file["path"]}`' for file in files)
                memory.append(dict(role='user', content=prompt))

        # load image (only support single image now)
        query_image_path = None
        for file in files:
            query_image_path = file['path']
        # if query_image_path end with 'png', type = png, else type = jpeg
        query_content = [
            {"type": "text", "text": query},
            {
                "type": "image",
                "image": f"file://{query_image_path}",
                "min_pixels": 256 * 28 * 28,
                "max_pixels": 1280 * 28 * 28
            },
        ]
        memory.append(dict(role='user', content=query_content)) 
        agent_return = self.agent.chat(memory)

        steps = []
        for action in agent_return.actions:
            if action.type == action_executor.finish_action.name:
                step = dict(role='assistant', content=action.format_result())
                steps.append(step)
            else:
                step = {'role': 'assistant'}
                args = action.args
                if action.errmsg is not None:
                    step['error'] = dict(type=action.state.name,
                                         msg=action.errmsg)
                    # Handle fallback args
                    args = args.get('inputs', args)
                function = dict(name=action.type, arguments=args)
                step['tool_calls'] = [dict(type='function', function=function)]
                steps.append(step)
                steps.append(dict(role='tool', content=action.result))
        return steps, memory
        

FORCE_STOP_PROMPT_EN = (
    """You should directly give results based on history information."""  # noqa
)

FEWSHOT_INSTRUCTION = """\
You are a assistant who can utilize external tools.
{tool_description}
To use a tool, please response with the following format:
```
{thought} Think what you need to solve, do you need to use tools?
{action} The tool name, should be one of [{action_names}].
{action_input} The input to the tool that you want to use.
```
The tool will give you response after your response using the following format:
```
{response} the results after call the tool.
```
Therefore DO NOT generate tool response by yourself.

Also please follow the guidelines:
1. Always use code interpreter to solve the problem.
2. The generated codes should always in a markdown code block format.
3. The generated codes will be executed in an ipython manner and the results will be cached.
4. Your responded code should always be simple and only solves the problem in current step.

Begin!
"""  # noqa

PYTHON_INTERPRETER_DESCRIPTION = """\
It can run a Python code. The code must be a valid code that contains only python method, and the method' name must be 'solution' and returns a dict, which key is variable name. The libraries I recommend are sympy and scipy. the format is:
```python
# import packages
import xxx
def solution():
    # initialize some variables
    variable_names_with_real_meaning = xxx
    # middle steps
    mid_variable = func(mid_variable)
    # final answer
    final_answer = func(mid_variable)
    return final_answer
```"""  # noqa


class CodeAgent(LagentAgent):
    """Code Agent wrapper for Lagent."""

    def __init__(self, llm, **kwargs):
        from lagent import PythonInterpreter, ReAct
        from lagent.agents.react import ReActProtocol

        agent_type = kwargs.pop('agent_type', ReAct)
        max_turn = kwargs.pop('max_turn', 3)
        actions = kwargs.pop(
            'actions',
            [
                dict(type=PythonInterpreter,
                     description=PYTHON_INTERPRETER_DESCRIPTION),
            ],
        )
        protocol = kwargs.pop(
            'protocol',
            dict(
                type=ReActProtocol,
                call_protocol=FEWSHOT_INSTRUCTION,
                force_stop=FORCE_STOP_PROMPT_EN,
                finish=dict(role='FINISH', begin='Final Answer:', end='\n'),
            ),
        )
        super().__init__(agent_type=agent_type,
                         llm=llm,
                         actions=actions,
                         protocol=protocol,
                         max_turn=max_turn,
                         **kwargs)
