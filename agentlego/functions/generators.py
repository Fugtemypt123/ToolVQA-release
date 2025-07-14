from .parsers import parser_map
from .examples import example_map
from .prompts import prompt_map
from .choices import choice_map, description_map
from .gpt import get_completion
from agentlego.tools.remote import RemoteTool
import re
import copy
from typing import Union
from functions.gentool import GENERATE_TOOLS
import random

random.seed(42)

class BaseGenerator:
    def __init__(self):
        pass

    def merge_context(self, contexts: list[dict]) -> str:
        return '\n'.join([f"{d['name']}: {parser_map[d['name']](d['input'], d['output'])}" for d in contexts])
    
    def merge_example(self, contexts: list[dict]) -> str:
        raise NotImplementedError("This method should be implemented in the child class.")

    def parse_result(self, tool: RemoteTool, image_path: str, result: str) -> tuple:
        raise NotImplementedError("This method should be implemented in the child class.")
    
    def parse_str(self, input_str: str) -> str:
        # for i in range(len(question)):
        #     if question[i].isalpha():
        #         question = question[i:]
        #         break
        # for i in range(len(question)-1, -1, -1):
        #     if question[i].isalpha() or question[i] == '?' or question[i] == '.':
        #         question = question[:i+1]
        #         break
        input_str = input_str.strip()
        input_str = input_str.replace('**', '').strip()
        input_str = input_str.replace('```', '').strip()
        input_str = input_str.replace('###', '').strip()
        # if input_str[-1] == '.' and input_str[-2].isdigit() and (input_str[-3].isdigit()==False):
        #     input_str = input_str[:-2]
        if '\n' in input_str:
            input_str = input_str.split('\n')[0]
        return input_str
    
    def get_lcs(self, now_node: str, alter_toolchain: list[str], now_toolchain: list[str]) -> int:
        # find lcs that ends with now_node, return the length of lcs and the end index of alter_toolchain
        n = len(alter_toolchain)
        m = len(now_toolchain)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if alter_toolchain[i - 1] == now_toolchain[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        pos_list = []
        next_set = set()
        for i in range(n, 0, -1):
            if alter_toolchain[i - 1] == now_node and (i==n or alter_toolchain[i] not in next_set):
                pos_list.append((dp[i][m], i-1))
                if i < n:
                    next_set.add(alter_toolchain[i])
        if len(pos_list) == 0:
            pos_list.append((0, -1))
        return pos_list

    def retrieve_example(self, now_node: str, contexts: str, image_type: str, num = 2) -> list[str]:
        context = self.merge_context(contexts)
        best_examples = []
        lcs_examples = []
        alter_examples = example_map[image_type]
        for i in range(len(alter_examples)):
            example = alter_examples[i]
            alter_toolchain = [d['name'] for d in example]
            now_toolchain = [d['name'] for d in contexts]
            pos_list = self.get_lcs(now_node, alter_toolchain, now_toolchain)
            lcs_examples.append(pos_list[0])
        # select top `num` best examples
        for i in range(num):
            max_lcs = -1
            max_id = -1
            for j in range(len(lcs_examples)):
                if lcs_examples[j][0] > max_lcs:
                    max_lcs = lcs_examples[j][0]
                    max_id = j
                    best_example = alter_examples[j][:lcs_examples[j][1] + 1]
            best_examples.append(self.merge_example(best_example))
            lcs_examples[max_id] = (-1, -1) # remove the selected example
        # put all contexts into padding_dict
        padding_dict = {}
        for i in range(num):
            example_name = f'example{i+1}'
            padding_dict[example_name] = best_examples[i] 
        padding_dict['context'] = context 
        return padding_dict

    def __call__(self, tool: RemoteTool, image_path: str, contexts: list[dict], image_type: str) -> dict:
        # select top 2 best examples
        padding_dict = self.retrieve_example(tool.name, contexts, image_type)
        prompt = prompt_map[tool.name].format(**padding_dict)
        result = get_completion(prompt)
        thought, input, output = self.parse_result(tool, image_path, result)
        return thought, input, output


class CalculatorGenerator(BaseGenerator):
    def __init__(self):
        super().__init__()

    def merge_example(self, contexts: list[dict]) -> str:
        result = "Information:\n"
        for d in contexts[:-1]:
            result += f"{d['name']}: {parser_map[d['name']](d['input'], d['output'])}\n"
        result += "\n"
        result += f"Thought: {contexts[-1]['thought_query']}\n"
        result += f"Formula: {contexts[-1]['input']['expression']}"
        return result

    def parse_result(self, tool: RemoteTool, image_path: str, result: str) -> tuple:
        formula = result.split('Formula:')[1].strip()
        formula = re.sub(r'[^0-9\.\+\-\*\/\(\)]', '', formula)
        formula = self.parse_str(formula)
        thought = result.split('Formula:')[0].split('Thought:')[1].strip()
        thought = self.parse_str(thought)
        output = tool(formula)
        input = {'expression': formula}
        return thought, input, output


class GoogleSearchGenerator(BaseGenerator):
    def __init__(self):
        super().__init__()

    def merge_example(self, contexts: list[dict]) -> str:
        result = "Information:\n"
        for d in contexts[:-1]:
            result += f"{d['name']}: {parser_map[d['name']](d['input'], d['output'])}\n"
        result += "\n"
        result += f"Thought: {contexts[-1]['thought_query']}\n"
        result += f"Query: {contexts[-1]['input']['query']}"
        return result

    def parse_result(self, tool: RemoteTool, image_path: str, result: str) -> tuple:
        query = result.split("Query:")[1].strip()
        query = self.parse_str(query)
        thought = result.split("Query:")[0].split('Thought:')[1].strip()
        thought = self.parse_str(thought)
        output = tool(query, 1).split('\n')[0]
        input = {'query': query}
        return thought, input, output


class PlotGenerator(BaseGenerator):
    def __init__(self):
        super().__init__()

    def merge_example(self, contexts: list[dict]) -> str:
        result = "Information:\n"
        for d in contexts[:-1]:
            result += f"{d['name']}: {parser_map[d['name']](d['input'], d['output'])}\n"
        result += "\n"
        result += f"Thought: {contexts[-1]['thought_query']}\n"
        result += f"Code: {contexts[-1]['input']['command']}"
        return result

    def parse_result(self, tool: RemoteTool, image_path: str, result: str) -> tuple:
        code = result.split('Code:')[1].strip()
        if '```python' in code:
            code = code.split('```python')[1].strip()
        if '```' in code:
            code = code.split('```')[0].strip()
        thought = result.split('Code:')[0].split('Thought:')[1].strip()
        thought = self.parse_str(thought)
        output = tool(code)
        input = {'command': code}
        return thought, input, output


class SolverGenerator(BaseGenerator):
    def __init__(self):
        super().__init__()

    def merge_example(self, contexts: list[dict]) -> str:
        result = "Information:\n"
        for d in contexts[:-1]:
            result += f"{d['name']}: {parser_map[d['name']](d['input'], d['output'])}\n"
        result += "\n"
        result += f"Thought: {contexts[-1]['thought_query']}\n"
        result += f"Code: {contexts[-1]['input']['command']}"
        return result

    def parse_result(self, tool: RemoteTool, image_path: str, result: str) -> tuple:
        code = result.split('Code:')[1].strip()
        thought = result.split('Code:')[0].split('Thought:')[1].strip()
        thought = self.parse_str(thought)
        output = tool(code)
        input = {'command': code}
        return thought, input, output


class OCRGenerator(BaseGenerator):
    def __init__(self):
        super().__init__()

    # 这里需要有一个小trick: 如果我们的image_path是中文图片的，我们就用中文ocr，否则英文
    def check_chinese(self, image_path: str) -> bool:
        CH_PATHS = ["/network_space/server126/shared/yinshaofeng/ToolLLM/GTA/datasets/MTWI/image_train"]
        for path in CH_PATHS:
            if image_path.startswith(path):
                return 'ch'
        return 'en'

    # 这里有一个python特性：只要函数的名称和参数数量一样，无论什么类型或参数名，都算重载
    def parse_result(self, tool: RemoteTool, image_path: str, prompt: str, image_type: str) -> tuple:
        thought = prompt
        lang = self.check_chinese(image_path)
        if image_type == 'no_obj_text':
            output = {'actual': tool(image_path, lang=lang), 'simple': tool(image_path, lang='qs')}
        else:
            output = tool(image_path, lang=lang)
        input = {'image': image_path}
        return thought, input, output

    def __call__(self, tool: RemoteTool, image_path: str, contexts: list[dict], image_type: str) -> dict:
        prompt = prompt_map[tool.name]
        thought, input, output = self.parse_result(tool, image_path, prompt, image_type)
        return thought, input, output


class ImageDescriptionGenerator(BaseGenerator):
    def __init__(self):
        super().__init__()

    def parse_result(self, tool: RemoteTool, image_path: str, prompt: str) -> tuple:
        thought = prompt
        output = tool(image_path)
        input = {'image': image_path}
        return thought, input, output

    def __call__(self, tool: RemoteTool, image_path: str, contexts: list[dict], image_type: str) -> dict:
        prompt = prompt_map[tool.name]
        thought, input, output = self.parse_result(tool, image_path, prompt)
        return thought, input, output


class TextToBboxGenerator(BaseGenerator):
    def __init__(self):
        super().__init__()

    def merge_example(self, contexts: list[dict]) -> str:
        result = "Information:\n"
        for d in contexts[:-1]:
            result += f"{d['name']}: {parser_map[d['name']](d['input'], d['output'])}\n"
        result += "\n"
        result += f"Thought: {contexts[-1]['thought_query']}\n"
        result += f"Object: {contexts[-1]['input']['text']}"
        return result

    def parse_result(self, tool: RemoteTool, image_path: str, result: str) -> tuple:
        obj = result.split('Object:')[1].strip()
        obj = self.parse_str(obj)
        thought = result.split('Object:')[0].split('Thought:')[1].strip()
        thought = self.parse_str(thought)
        output = tool(image_path, obj)
        input = {'image': image_path, 'text': obj}
        return thought, input, output


class CountGivenObjectGenerator(BaseGenerator):
    def __init__(self):
        super().__init__()

    def merge_example(self, contexts: list[dict]) -> str:
        result = "Information:\n"
        for d in contexts[:-1]:
            result += f"{d['name']}: {parser_map[d['name']](d['input'], d['output'])}\n"
        result += "\n"
        result += f"Thought: {contexts[-1]['thought_query']}\n"
        result += f"Object: {contexts[-1]['input']['text']}"
        return result

    def parse_result(self, tool: RemoteTool, image_path: str, result: str) -> tuple:
        obj = result.split('Object:')[1].strip()
        obj = self.parse_str(obj)
        thought = result.split('Object:')[0].split('Thought:')[1].strip()
        thought = self.parse_str(thought)
        output = tool(image_path, obj)
        input = {'image': image_path, 'text': obj}
        return thought, input, output


class MathOCRGenerator(BaseGenerator):
    def __init__(self):
        super().__init__()

    def parse_result(self, tool: RemoteTool, image_path: str, prompt: str) -> tuple:
        thought = prompt
        output = tool(image_path)
        input = {'image': image_path}
        return thought, input, output

    def __call__(self, tool: RemoteTool, image_path: str, contexts: list[dict], image_type: str) -> dict:
        prompt = prompt_map[tool.name]
        thought, input, output = self.parse_result(tool, image_path, prompt)
        return thought, input, output


class DrawBoxGenerator(BaseGenerator):
    def __init__(self):
        super().__init__()

    def merge_example(self, contexts: list[dict]) -> str:
        result = "Information:\n"
        for d in contexts[:-1]:
            result += f"{d['name']}: {parser_map[d['name']](d['input'], d['output'])}\n"
        result += "\n"
        result += f"Thought: {contexts[-1]['thought_query']}\n"
        result += f"Bounding Box: {contexts[-1]['input']['bbox']}"
        return result

    def parse_result(self, tool: RemoteTool, image_path: str, result: str) -> tuple:
        bbox = result.split('Bounding Box:')[1].strip()
        bbox = self.parse_str(bbox)
        thought = result.split('Bounding Box:')[0].split('Thought:')[1].strip()
        thought = self.parse_str(thought)
        output = tool(image_path, bbox)
        input = {'image': image_path, 'bbox': bbox}
        return thought, input, output


class AddTextGenerator(BaseGenerator):
    def __init__(self):
        super().__init__()

    def merge_example(self, contexts: list[dict]) -> str:
        result = "Information:\n"
        for d in contexts[:-1]:
            result += f"{d['name']}: {parser_map[d['name']](d['input'], d['output'])}\n"
        result += "\n"
        result += f"Thought: {contexts[-1]['thought_query']}\n"
        result += f"Text: {contexts[-1]['input']['text']}\n"
        result += f"Position: {contexts[-1]['input']['position']}"
        return result

    def parse_result(self, tool: RemoteTool, image_path: str, result: str) -> tuple:
        position = result.split('Position:')[1].strip()
        position = self.parse_str(position)
        text = result.split('Position:')[0].split('Text:')[1].strip()
        thought = result.split('Position:')[0].split('Text:')[0].split('Thought:')[1].strip()
        thought = self.parse_str(thought)
        output = tool(image_path, text, position)
        input = {'image': image_path, 'text': text, 'position': position}
        return thought, input, output


class TextToImageGenerator(BaseGenerator):
    def __init__(self):
        super().__init__()

    def merge_example(self, contexts: list[dict]) -> str:
        result = "Information:\n"
        for d in contexts[:-1]:
            result += f"{d['name']}: {parser_map[d['name']](d['input'], d['output'])}\n"
        result += "\n"
        result += f"Thought: {contexts[-1]['thought_query']}\n"
        result += f"Keywords: {contexts[-1]['input']['keywords']}"
        return result

    def parse_result(self, tool: RemoteTool, image_path: str, result: str) -> tuple:
        keywords = result.split('Keywords:')[1].strip()
        keywords = self.parse_str(keywords)
        keywords = keywords.split(',')
        if len(keywords) > 4:
            keywords = keywords[:4]
        thought = result.split('Keywords:')[0].split('Thought:')[1].strip()
        thought = self.parse_str(thought)
        output = tool(keywords)
        input = {'keywords': keywords}
        return thought, input, output


class ImageStylizationGenerator(BaseGenerator):
    def __init__(self):
        super().__init__()

    def merge_example(self, contexts: list[dict]) -> str:
        result = "Information:\n"
        for d in contexts[:-1]:
            result += f"{d['name']}: {parser_map[d['name']](d['input'], d['output'])}\n"
        result += "\n"
        result += f"Thought: {contexts[-1]['thought_query']}\n"
        result += f"Instruction: {contexts[-1]['input']['instruction']}"
        return result

    def parse_result(self, tool: RemoteTool, image_path: str, result: str) -> tuple:
        instruction = result.split('Instruction:')[1].strip()
        instruction = self.parse_str(instruction)
        thought = result.split('Instruction:')[0].split('Thought:')[1].strip()
        thought = self.parse_str(thought)
        output = tool(image_path, instruction)
        input = {'image': image_path, 'instruction': instruction}
        return thought, input, output


class RegionAttributeDescriptionGenerator(BaseGenerator):
    def __init__(self):
        super().__init__()

    def merge_example(self, contexts: list[dict]) -> str:
        result = "Information:\n"
        for d in contexts[:-1]:
            result += f"{d['name']}: {parser_map[d['name']](d['input'], d['output'])}\n"
        result += "\n"
        result += f"Thought: {contexts[-1]['thought_query']}\n"
        result += f"Bounding Box: {contexts[-1]['input']['bbox']}\n"
        result += f"Attribute: {contexts[-1]['input']['attribute']}"
        return result

    def parse_result(self, tool: RemoteTool, image_path: str, result: str) -> tuple:
        attribute = result.split('Attribute:')[1].strip()
        attribute = self.parse_str(attribute)
        bbox = result.split('Attribute:')[0].split('Bounding Box:')[1].strip()
        bbox = self.parse_str(bbox)
        thought = result.split('Attribute:')[0].split('Bounding Box:')[0].split('Thought:')[1].strip()
        thought = self.parse_str(thought)
        output = tool(image_path, bbox, attribute)
        input = {'image': image_path, 'bbox': bbox, 'attribute': attribute}
        return thought, input, output


class QuestionGenerator(BaseGenerator):
    def __init__(self):
        super().__init__()

    # def merge_context(self, contexts: list[dict]) -> str:
        # return '\n'.join([f"{d['name']}:\nThought: {d['thought']}\nInput: {d['input']}\nOutput: {parser_map[d['name']](d['input'], d['output'])}" for d in contexts])

    def merge_example(self, contexts: list[dict]) -> str:
        result = "Information:\n"
        for d in contexts[:-1]:
            # result += f"{d['name']}:\nThought: {d['thought_query']}\nInput: {d['input']}\nOutput: {parser_map[d['name']](d['input'], d['output'])}\n"
            result += f"{d['name']}: {parser_map[d['name']](d['input'], d['output'])}\n"
        result += "\n"
        result += f"Thought: {contexts[-1]['thought']}\n"
        result += f"Question: {contexts[-1]['question']}\n"
        result += f"Answer: {contexts[-1]['answer']}"
        return result
    
    def parse_result(self, result: str) -> tuple:
        answer = result.split('Answer:')[1].strip()
        question = result.split('Answer:')[0].split('Question:')[1].strip()
        thought = result.split('Question:')[0].split('Thought:')[1].strip()
        thought = self.parse_str(thought)
        question = self.parse_str(question)
        answer = self.parse_str(answer)
        return thought, question, answer

    def __call__(self, contexts: list[dict], image_type: str) -> dict:
        padding_dict = self.retrieve_example(now_node='Question', contexts=contexts, image_type=image_type)
        padding_dict['examples'] = ""
        for i in range(2):
            example_name = f'example{i+1}'
            padding_dict['examples'] += f"Example {i+1}:\n```\n{padding_dict[example_name]}\n```\n\n"
        if contexts[-1]['name'] in GENERATE_TOOLS.keys():
            padding_dict['examples'] += f"""**NOTE:** you are now asked to generate an image, so your question stem must explicitly include the verbs "generate" or "plot" or "circle" (depending on which tool was used last), and your answer must be 'image/output.png'.\nTo ask a good generate image question, you should refer to the thought of the last tool call and come up with a creative question from it, rather than just copying the information given."""
        prompt = prompt_map['Question'].format(**padding_dict)
        result = get_completion(prompt)
        thought, question, answer = self.parse_result(result)
        return thought, question, answer


class RethinkQuestionGenerator(BaseGenerator):
    def __init__(self):
        super().__init__()
        self.example_id = 0

    def merge_context(self, contexts: list[dict], ori_question: str) -> str:
        if contexts[0]['name'] != 'ImageDescription':
            return f"You dont need to modify the question since the first tool is not ImageDescription. Please output the original question by the following format:\nThought: None\nAdjusted Question: {ori_question}\n"
        result = f"ImageDescription: {parser_map[contexts[0]['name']](contexts[0]['input'], contexts[0]['output'])}\n"
        result += f"Original Question: {ori_question}\n"
        return result

    # def merge_example(self, contexts: list[dict]) -> str:
    #     self.example_id += 1
    #     # result = f"Information:\n"
    #     result = ""
    #     for d in contexts[:1]:
    #         result += f"{d['name']}: {parser_map[d['name']](d['input'], d['output'])}\n"
    #     result += f"Original Question: {contexts[-1]['ori_question']}\n\n"
    #     result += f"Thought: {contexts[-1]['rethink']}\n"
    #     result += f"Adjusted Question: {contexts[-1]['question']}"
    #     return result
    
    def parse_result(self, result: str) -> tuple:
        question = result.split('Adjusted Question:')[1].strip()
        thought = result.split('Adjusted Question:')[0].split('Thought:')[1].strip()
        thought = self.parse_str(thought)
        question = self.parse_str(question)
        question = question.replace('3.', '')
        return thought, question
    
    def __call__(self, contexts: list[dict], ori_question: str, answer: str, image_type: str) -> str:
        if contexts[0]['name'] != 'ImageDescription':
            return None, ori_question
        self.example_id = 0
        # padding_dict = self.retrieve_example(now_node='Question', contexts=contexts, image_type=image_type)
        padding_dict = {'context': self.merge_context(contexts, ori_question)}
        # padding_dict['question'] = ori_question
        # padding_dict['answer'] = answer
        prompt = prompt_map['RethinkQuestion'].format(**padding_dict)
        result = get_completion(prompt)
        thought, question = self.parse_result(result)
        return thought, question


class ThoughtGenerator(BaseGenerator):
    def __init__(self):
        super().__init__()

    def merge_context(self, contexts: list[dict]) -> str:
        return '\n'.join([f"{d['name']}:\nInput: {d['input']}\nOutput: {parser_map[d['name']](d['input'], d['output'])}" for d in contexts])

    def parse_result(self, result: str, context: list[dict]) -> list[dict]:
        for d in reversed(context):
            split_str = d['name'] + ':'
            thought = result.split(split_str)[-1].strip()
            thought = self.parse_str(thought)
            d['thought_query'] = d['thought']
            d['thought'] = thought
            if len(result.split(split_str)) > 1:
                result = result.split(split_str)[-2].strip()
        return context
    
    def merge_example(self, contexts: list[dict]) -> str:
        result = f"Question: {contexts[-1]['question']}\n\nSolving Process:\n"
        for d in contexts[:-1]:
            result += f"{d['name']}:\nInput: {d['input']}\nOutput: {parser_map[d['name']](d['input'], d['output'])}\n"
        result += f"\nAnswer: {contexts[-1]['answer']}\n\nThinking Process:"
        for d in contexts[:-1]:
            result += f"\n{d['name']}: {d['thought']}"
        return result

    def __call__(self, question: str, answer: str, contexts: list[dict], image_type: str) -> list[dict]:
        padding_dict = self.retrieve_example(now_node='Question', contexts=contexts, image_type=image_type)
        padding_dict['question'] = question
        padding_dict['answer'] = answer
        prompt = prompt_map['Thought'].format(**padding_dict)
        result = get_completion(prompt)
        final_contexts = self.parse_result(result, contexts)
        return final_contexts


class NextStepGenerator(BaseGenerator):
    def __init__(self):
        super().__init__()

    def merge_choice(self, choices: list[str]) -> str:
        return '\n'.join([f"{i+1}. {choices[i]}: {description_map[choices[i]]}" for i in range(len(choices))])

    def parse_result(self, result: str, now_node: str, image_type: str) -> tuple:
        next_tool = result.split('Choice:')[1].strip()
        next_tool = self.parse_str(next_tool)
        thought = result.split('Choice:')[0].split('Thought:')[1].strip()
        thought = self.parse_str(thought)
        # remove all non-alphabetic characters in next_tool
        number, name = next_tool.split('.')
        # remove all non-int characters in number
        number = re.sub(r'\D', '', number)
        # find the choice which has max lcs with the next_tool
        number = int(number)
        name = name.strip()
        gt_name = choice_map[image_type][now_node][number-1]
        # if gt_name != name:
        #     print(f"Warning: The selected tool is not the same as the ground truth. GT: ({gt_name} {len(gt_name)}), Selected: ({name} {len(name)})")
        return thought, gt_name

    def merge_example(self, contexts: list[dict], image_type: str) -> str:
        result = "Information:\n"
        for d in contexts[:-1]:
            result += f"{d['name']}: {parser_map[d['name']](d['input'], d['output'])}\n"
        result += "\n"
        result += f"Thought: {contexts[-2]['thought_choose']}\n"
        choices = choice_map[image_type][contexts[-2]['name']]
        # find the choice that is the same as the last tool
        index = 0
        last_name = None
        for i in range(len(choices)):
            if choices[i] == contexts[-1]['name']:
                index = i+1
                last_name = choices[i]
        result += f"Choice: {index}. {last_name}"
        return result

    def retrieve_example(self, now_node: str, contexts: str, image_type: str) -> list[str]:
        context = self.merge_context(contexts)
        best_examples = []
        lcs_examples = []
        alter_examples = example_map[image_type]
        for i in range(len(alter_examples)):
            example = alter_examples[i]
            alter_toolchain = [d['name'] for d in example]
            now_toolchain = [d['name'] for d in contexts]
            pos_list = self.get_lcs(now_node, alter_toolchain, now_toolchain)
            lcs_examples.append(pos_list)
        # select examples for each choice
        unvis_choices = choice_map[image_type][now_node]
        for i in range(len(unvis_choices)):
            max_lcs = -1
            best_example = None
            for j in range(len(lcs_examples)):
                for k in range(len(lcs_examples[j])):
                    if lcs_examples[j][k][0] > max_lcs and alter_examples[j][lcs_examples[j][k][1] + 1]['name'] == unvis_choices[i]:
                        max_lcs = lcs_examples[j][k][0]
                        best_example = alter_examples[j][:lcs_examples[j][k][1] + 2] # add one more tool for NEXT step
            best_examples.append(self.merge_example(best_example, image_type))
            # if max_lcs == -1:
            #     print(f"Warning: Cannot find the {i+1}-th choices' example.")

        # put all contexts into padding_dict
        padding_dict = {}
        padding_dict['examples'] = ""
        for i in range(len(unvis_choices)):
            if i < len(unvis_choices) - 1:
                now_example = f"Example {i+1}:\n```\n{best_examples[i]}\n```\n\n"
            else:
                now_example = f"Example {i+1}:\n```\n{best_examples[i]}\n```"
            padding_dict['examples'] += now_example
        padding_dict['context'] = context 
        return padding_dict

    def heuristic_filter(self, now_choice_map: list[str], contexts: list[dict]) -> list[str]:
        # randomly remove GENERATE_TOOLS
        for choice in now_choice_map:
            if choice in GENERATE_TOOLS.keys():
                random_num = random.random()
                if random_num < 0.5:
                    now_choice_map.remove(choice)
                    break    
        # remove question to promote longer tool-chain
        # if 'Question' in now_choice_map and len(now_choice_map) > 1 and len(contexts) < 3:
        #     # 50% remove Question
        #     random_num = random.random()
        #     if random_num < 0.5:
        #         now_choice_map.remove('Question')
        return now_choice_map

    def __call__(self, now_node: str, contexts: list[dict], image_type: str) -> str:
        # special case: only one choice
        now_choice_map = copy.deepcopy(choice_map[image_type][now_node])
        now_choice_map = self.heuristic_filter(now_choice_map, contexts)
        if len(now_choice_map) == 1:
            thought = "There is only one choice, so we will directly use it."
            return thought, now_choice_map[0]
        padding_dict = self.retrieve_example(now_node=now_node, contexts=contexts, image_type=image_type)
        options = self.merge_choice(now_choice_map)
        padding_dict['options'] = options
        prompt = prompt_map['NextStep'].format(**padding_dict)
        result = get_completion(prompt, model='gpt-3.5-turbo-1106')
        thought, next_tool = self.parse_result(result, now_node, image_type)
        return thought, next_tool


generator_map = {
    'Calculator': CalculatorGenerator(),
    'GoogleSearch': GoogleSearchGenerator(),
    'Plot': PlotGenerator(),
    'Solver': SolverGenerator(),
    'OCR': OCRGenerator(),
    'ImageDescription': ImageDescriptionGenerator(),
    'TextToBbox': TextToBboxGenerator(),
    'CountGivenObject': CountGivenObjectGenerator(),
    'MathOCR': MathOCRGenerator(),
    'DrawBox': DrawBoxGenerator(),
    'AddText': AddTextGenerator(),
    'TextToImage': TextToImageGenerator(),
    'ImageStylization': ImageStylizationGenerator(),
    'RegionAttributeDescription': RegionAttributeDescriptionGenerator(),
    'Question': QuestionGenerator(),
    'RethinkQuestion': RethinkQuestionGenerator(),
    'Thought': ThoughtGenerator(),
    'NextStep': NextStepGenerator(),
}