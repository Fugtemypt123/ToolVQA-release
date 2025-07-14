import json
import random

with open('dataset.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

def add_user_prefix(user_prompt: str):
    return f"<image>\n{user_prompt}"

CALL_PROTOCOL_EN = """You are a assistant who can utilize external tools.
{tool_description}
To use a tool, please use the following format:
```
Thought:Think what you need to solve, do you need to use tools?
Action:the tool name, should be one of [{action_names}]
Action Input:the input to the action
```
The response after utilizing tools should using the following format:
```
Tool Response:the results after call the tool.
```
If you already know the answer, or you do not need to use tools,
please using the following format to reply:
```
Thought:the thought process to get the final answer
Final Answer:final answer
```
Begin!"""

# CALL_PROTOCOL_EN = """You are a assistant who can utilize external tools.
# {tool_description}
# To use a tool, please use the following format:
# ```
# Call {{tool_name}} with arguments {{arguments}}
# ```
# The response after utilizing tools should using the following format:
# ```
# Tool Response:the results after call the tool.
# ```
# If you already know the answer, or you do not need to use tools,
# please using the following format to reply:
# ```
# Final Answer:final answer
# ```
# Begin!"""

def format_result(result):
    res = []
    if result['type'] == 'text':
        res.append(result['content'])
    else:
        res.append(f"[{result['type']}]({result['content']})")
    res = '\n'.join(res)
    return res

def convert_to_training_format(data):
    conversations = []
    # 生成工具描述字符串
    num = 0

    for key, entry in data.items():
        # if 'image/output.png' in entry['gt_answer']['whitelist']:
        #     continue
        conversation = []
        tools_description = json.dumps(entry['tools'])
        name_list = [d['name'] for d in entry['tools']]
        action_names = json.dumps(name_list)
        FirstRound = True
        image_path = entry['files'][0]['path']
        if not image_path.endswith('.jpg'):
            # change the file name in the os to jpg
            print(image_path)
            import os
            if os.path.exists(image_path):
                os.rename(image_path, image_path.split('.')[0] + '.jpg')
            image_path = image_path.split('.')[0] + '.jpg'
        conversation.append({
            "from": 'human',
            'value': CALL_PROTOCOL_EN.format(tool_description=tools_description, action_names=action_names) + '\nThe related files are at `{}`\n'.format(image_path)
        })
        # 遍历对话记录
        for dialog in entry["dialogs"]:
            if dialog["role"] == "user":
                if FirstRound:
                    conversation[-1]["value"] += add_user_prefix(dialog["content"]).replace("'", '"')
                else:
                    conversation.append({"input": add_user_prefix(dialog["content"])})
            elif dialog["role"] == "assistant":
                if "tool_calls" in dialog:
                    for tool_call in dialog["tool_calls"]:
                        if tool_call["type"] == "function":
                            tool_name = tool_call["function"]["name"]
                            arguments = tool_call["function"]["arguments"]
                            if 'thought' not in dialog.keys():
                                thought = ""
                            else:
                                thought = dialog["thought"]
                            if "image" in arguments:
                                arguments["image"] = image_path
                            # conversation[-1]["output"] = f"Call {tool_name} with arguments {arguments}"
                            conversation.append({
                                'from': 'gpt',
                                'value': f"Thought:{thought}\nAction:{tool_name}\nAction Input:```json\n{arguments}\n```".replace("'", '"')
                            })
                else:
                    thought = "Now that we have all the information to solve the problem, we can get our final answer."
                    # conversation[-1]["output"] = f"Final Answer:{dialog['content']}"
                    conversation.append({
                        'from': 'gpt',
                        'value': f"Thought:{thought}\nFinal Answer:{dialog['content']}".replace("'", '"')
                    })
            elif dialog["role"] == "tool":
                # 将工具输出直接作为字符串输入
                conversation.append({
                    'from': 'human',
                    "value": f"Tool Response:{format_result(dialog['content'])}".replace("'", '"')})
            FirstRound = False
        conversations.append({"image": image_path, "id": num, "conversations": conversation})
        num += 1
        # if num >= 10000-7721:
        #     break
    
    return conversations

training_data = convert_to_training_format(data)

with open(f'train/gta_{len(training_data)}.json', 'w', encoding='utf-8') as f:
    json.dump(training_data, f, ensure_ascii=False, indent=4)

print(f"转换完成，数据已保存到 gta_{len(training_data)}.json。")
