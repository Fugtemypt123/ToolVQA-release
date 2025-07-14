# 将我们的数据集转换成gta的格式以便测试

import json
import random

with open('train/last_7721.json', 'r') as f:
    dataset = json.load(f)
    random.shuffle(dataset)

with open('toolmeta.json', 'r') as f:
    toolset = json.load(f)

GENERATE_TOOLS = ["ImageStylization", "TextToImage", "DrawBox", "AddText", "Plot"]

# with open('datasets/test_ingta.json', 'r') as f:
#     new_dataset = json.load(f)

# num = len(new_dataset)
# print(num)
# print(len(dataset))
new_dataset = {
}
num = 0

for i in range(len(dataset)):
    data = dataset[i]
    new_dataset[num] = {}
    new_dataset[num]['tools'] = []
    # for tool_name in tool_map[data['type']]:
    #     new_dataset[num]['tools'].append(toolset[tool_name])
    new_dataset[num]['files'] = [{
        'type': 'image',
        'path': data['image_path'],
        'url': None
    }]
    # if data['better_ques'] == 1:
    #     ques = data['question']
    # else:
    #     ques = data['ori_question']

    ques = data['question']
    new_dataset[num]['dialogs'] = [{
        'role': 'user',
        'content': ques
    }]
    for j in range(len(data['context'])):
        new_dataset[num]['dialogs'].append({
            'role': 'assistant',
            "tool_calls": [{
                "type": "function",
                "function": {
                    "name": data['context'][j]['name'],
                    "arguments": data['context'][j]['input']
                }
            }],
            'thought': data['context'][j]['thought']
        })
        new_dataset[num]['dialogs'].append({
            'role': 'tool',
            'name': data['context'][j]['name'],
            'content': {
                'type': toolset[data['context'][j]['name']]['outputs'][0]['type'],
                'content': data['context'][j]['output']
            }
        })
        new_dataset[num]['tools'].append(toolset[data['context'][j]['name']])
    new_dataset[num]['dialogs'].append({
        'role': 'assistant',
        'content': data['answer']
    })
    new_dataset[num]['gt_answer'] = {
        'whitelist': [[data['answer']]],
        'blacklist': None
    }
    num += 1

    # if data['context'][-1]['name'] not in GENERATE_TOOLS:
    #     new_dataset[num]['gt_answer'] = {
    #         'whitelist': [[data['answer']]],
    #         'blacklist': None
    #     }
    # else:
    #     new_dataset[num]['gt_answer'] = None

print(len(new_dataset))

with open('train/new_7721.json', 'w') as f:
    json.dump(new_dataset, f, indent=4)
    
# new_dataset_prefix = {}

# for i in range(46):
#     new_dataset_prefix[num] = new_dataset[num]

# with open('datasets/test_ingta_46.json', 'w') as f:
#     json.dump(new_dataset_prefix, f, indent=4)

# for i in range(46, 92):
#     new_dataset_prefix[num] = new_dataset[num]

# with open('datasets/test_ingta_92.json', 'w') as f:
#     json.dump(new_dataset_prefix, f, indent=4)