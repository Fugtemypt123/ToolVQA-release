import json
import time
import random
from agentlego.tools.remote import RemoteTool
from functions.generators import generator_map
from functions.gentool import GENERATE_TOOLS
import copy

ERROR_UPPER_BOUND = 3 # 3

# tool_id = args.idx + 16180

def build_epoch(server_id, epoch_id, datas):
    # Toolset = RemoteTool.from_server('http://0.0.0.0:{}'.format(16181 + server_id))
    Toolset = RemoteTool.from_server('http://0.0.0.0:16181')
    tools = {}
    for tool in Toolset:
        tools[tool.name] = RemoteTool.from_url(tool.url)

    generate_tools = copy.deepcopy(GENERATE_TOOLS)
    tools.update(generate_tools)
    random.seed(42)

    if len(datas) == 0:
        print("Warning: No data provided, using default data.")
        with open('../datasets/datas_sample100.json', 'r') as f:
            datas = json.load(f)

    num = 0 
    dataset = []

    # add a timer to record the time cost
    start = time.time()

    for data in datas:
        image_path = data['image']
        image_type = data['tag']

        num += 1

        if epoch_id == 0:
            print("Processing image: ", num)
            print("Time Cost: ", time.time() - start)
            print("Successfully processed: ", len(dataset)) 

        now_node = 'Start'
        now_context = [] 
        tool_chain = []
        error_times = 0
        max_length = 8
        
        for _ in range(max_length):          
            try:
                thought_choose, next_node = generator_map['NextStep'](now_node, now_context, image_type)
                if next_node == 'Question':
                    break
                tool = tools[next_node]
                thought, input, output = generator_map[next_node](tool, image_path, now_context, image_type) 
                # NOTE: In order to ask high-quality questions, we may simplify the output of the tool, in which case we will keep two versions of the output
                if isinstance(output, dict):
                    now_context.append(
                        {
                            'name': next_node,
                            'thought': thought,
                            'thought_choose': thought_choose,
                            'input': input,
                            'output': output['simple'],
                            'actual_output': output['actual']
                        }
                    )
                else:
                    now_context.append(
                        {
                            'name': next_node,
                            'thought': thought,
                            'thought_choose': thought_choose,
                            'input': input,
                            'output': output,
                        }
                    )
                # print("Next Node: ", next_node, "Time Cost: ", time.time() - start)
                tool_chain.append(next_node)
                now_node = next_node

            except Exception as e:
                if epoch_id == 0:
                    print("Error:", e)
                error_times += 1
                if error_times >= ERROR_UPPER_BOUND:
                    break
                continue

        if error_times >= ERROR_UPPER_BOUND:
            continue
            
        try:
            thought_question, question, final_answer = generator_map['Question'](now_context, image_type)
            # thought_rethink, final_question = generator_map['RethinkQuestion'](now_context, question, final_answer, image_type)
            final_question = question
            final_context = generator_map['Thought'](final_question, final_answer, now_context, image_type)

            # TODO: turn the data into ReAct format
            data = {
                'image_path': image_path,
                'context': final_context,
                'question': final_question,
                # 'ori_question': question,
                # 'thought_rethink': thought_rethink,
                'thought_question': thought_question,
                'answer': final_answer,
                'type': image_type
            }
            dataset.append(data)

        except Exception as e:
            if epoch_id == 0:
                print(e)
            continue

        # if epoch_id == 0:
        #     print("Successfully processed: ", len(dataset))
    
        with open(f'generated_data/data_{epoch_id}.json', 'w') as f:
            json.dump(dataset, f, indent=4) 


def build_epoch_fixed(server_id, epoch_id, fixed_chain, fixed_type, datas):
    # fixed_chain: ['Tool1', 'Tool2', 'Tool3', 'Tool4', 'Question']
    # fixed_type: ['type1', 'type2', 'type3', 'type4']

    # Toolset = RemoteTool.from_server('http://0.0.0.0:{}'.format(16181 + server_id))
    Toolset = RemoteTool.from_server('http://0.0.0.0:16181')
    tools = {}
    for tool in Toolset:
        tools[tool.name] = RemoteTool.from_url(tool.url)

    generate_tools = copy.deepcopy(GENERATE_TOOLS)
    tools.update(generate_tools)
    random.seed(42)

    if len(datas) == 0:
        print("Warning: No data provided, using default data.")
        with open('../datasets/datas_sample100.json', 'r') as f:
            datas = json.load(f)

    num = 0 
    dataset = []

    # add a timer to record the time cost
    start = time.time()

    for data in datas:
        image_path = data['image']
        image_type = data['tag']
        if image_type not in fixed_type:
            continue

        num += 1

        if epoch_id == 0:
            print("Processing image: ", num)
            print("Time Cost: ", time.time() - start)
            print("Successfully processed: ", len(dataset)) 

        now_context = [] 
        tool_chain = []
        error_times = 0
        idx = 0
        
        while True:          
            try:
                # thought_choose, next_node = generator_map['NextStep'](now_node, now_context, image_type)
                thought_choose = None
                next_node = fixed_chain[idx]
                if next_node == 'Question':
                    break
                tool = tools[next_node]
                thought, input, output = generator_map[next_node](tool, image_path, now_context, image_type) 
                # NOTE: In order to ask high-quality questions, we may simplify the output of the tool, in which case we will keep two versions of the output
                if isinstance(output, dict):
                    now_context.append(
                        {
                            'name': next_node,
                            'thought': thought,
                            'thought_choose': thought_choose,
                            'input': input,
                            'output': output['simple'],
                            'actual_output': output['actual']
                        }
                    )
                else:
                    now_context.append(
                        {
                            'name': next_node,
                            'thought': thought,
                            'thought_choose': thought_choose,
                            'input': input,
                            'output': output,
                        }
                    )
                # print("Next Node: ", next_node, "Time Cost: ", time.time() - start)
                tool_chain.append(next_node)
                idx += 1

            except Exception as e:
                if epoch_id == 0:
                    print("Error:", e)
                error_times += 1
                if error_times >= ERROR_UPPER_BOUND:
                    break
                continue

        if error_times >= ERROR_UPPER_BOUND:
            continue
            
        try:
            thought_question, question, final_answer = generator_map['Question'](now_context, image_type)
            # thought_rethink, final_question = generator_map['RethinkQuestion'](now_context, question, final_answer, image_type)
            final_question = question
            final_context = generator_map['Thought'](final_question, final_answer, now_context, image_type)

            # TODO: turn the data into ReAct format
            data = {
                'image_path': image_path,
                'context': final_context,
                'question': final_question,
                'thought_question': thought_question,
                'answer': final_answer,
                'type': image_type
            }
            dataset.append(data)

        except Exception as e:
            if epoch_id == 0:
                print(e)
            continue

        # if epoch_id == 0:
        #     print("Successfully processed: ", len(dataset))
    
        with open(f'generated_data/fix_chain/fixdata_{epoch_id}.json', 'w') as f:
            json.dump(dataset, f, indent=4) 

if __name__ == "__main__":
    build_epoch(0, 0, [])