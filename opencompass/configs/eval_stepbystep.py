from lagent.agents import ReAct
from mmengine.config import read_base

from opencompass.models import OpenAI, Qwen, Gemini, OpenAIVisual, OpenAIVisualDummy
from opencompass.models.lagent import LagentAgent, LagentAgentVisual, LagentAgentVisualLocal
from opencompass.partitioners import SizePartitioner
from opencompass.runners import LocalRunner
from opencompass.tasks import OpenICLInferTask

with read_base():
    from .datasets.gta_bench_stepbystep import gta_bench_datasets as datasets

import os
api_key = os.getenv('OPENAI_API_KEY')

models = {
    # 没有vlm setting

    ######################### Dummy VLM / Tool VLM #########################
    
    'llava-ft-100_vlm_tool_stepbystep': dict(
        abbr='llava-ft-100_vlm_tool',
        type=LagentAgentVisualLocal,
        agent_type=ReAct,
        max_turn=6,
        llm=dict(
            type=OpenAIVisual,
            path='llava-ft-100',
            key='EMPTY', # put your key here
            openai_api_base='http://222.29.51.126:12581/v1',
            query_per_second=1,
            max_seq_len=3072,
            stop='<|eot_id|>',
        ),
        # tool_server='http://222.29.51.126:16181', # end-to-end
        tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),
    'llava-ft-1000_vlm_tool_stepbystep': dict(
        abbr='llava-ft-1000_vlm_tool',
        type=LagentAgentVisualLocal,
        agent_type=ReAct,
        max_turn=6,
        llm=dict(
            type=OpenAIVisual,
            path='llava-ft-1000',
            key='EMPTY', # put your key here
            openai_api_base='http://222.29.51.126:12582/v1',
            query_per_second=1,
            max_seq_len=3072,
            stop='<|eot_id|>',
        ),
        # tool_server='http://222.29.51.126:16181', # end-to-end
        tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),
    'llava-ft-53760_vlm_tool_stepbystep': dict(
        abbr='llava-ft-53760_vlm_tool',
        type=LagentAgentVisualLocal,
        agent_type=ReAct,
        max_turn=6,
        llm=dict(
            type=OpenAIVisual,
            path='llava-ft-53760',
            key='EMPTY', # put your key here
            openai_api_base='http://222.29.51.126:12581/v1',
            query_per_second=1,
            max_seq_len=3072,
            stop='<|eot_id|>',
        ),
        # tool_server='http://222.29.51.126:16181', # end-to-end
        tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),
    'llava-ft-nocaption_vlm_tool_stepbystep': dict(
        abbr='llava-ft-nocaption_vlm_tool',
        type=LagentAgentVisualLocal,
        agent_type=ReAct,
        max_turn=6,
        llm=dict(
            type=OpenAIVisual,
            path='llava-ft-nocaption',
            key='EMPTY', # put your key here
            openai_api_base='http://222.29.51.128:12587/v1',
            query_per_second=1,
            max_seq_len=3072,
            stop='<|eot_id|>',
        ),
        # tool_server='http://222.29.51.126:16181', # end-to-end
        tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),
    'chatgpt-4o-latest_vlm_tool_stepbystep': dict(
        abbr='chatgpt-4o-latest_vlm_tool_stepbystep',
        type=LagentAgentVisual,
        agent_type=ReAct,
        max_turn=6,
        llm=dict(
            type=OpenAIVisual,
            path='chatgpt-4o-latest',
            key=api_key, # put your key here
            openai_api_base='https://29qg.com/v1',
            query_per_second=1,
            max_seq_len=4096,
            retry=10
        ),
        # end-to-end
        tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),
    'claude-3-5-sonnet_vlm_tool_stepbystep': dict(
        abbr='claude-3-5-sonnet_vlm_tool_sbs',
        type=LagentAgentVisual,
        agent_type=ReAct,
        max_turn=6,
        llm=dict(
            type=OpenAIVisual,
            path='claude-3-5-sonnet-20240620',
            key=api_key, # put your key here
            openai_api_base='https://29qg.com/v1',
            query_per_second=1,
            max_seq_len=4096,
            retry=10
        ),# end-to-end
        tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),
    'gpt-4o_vlm_tool_stepbystep': dict(
        abbr='gpt-4o_vlm_tool_stepbystep',
        type=LagentAgentVisual,
        agent_type=ReAct,
        max_turn=6,
        llm=dict(
            type=OpenAIVisual,
            path='gpt-4o',
            key=api_key, # put your key here
            openai_api_base='https://29qg.com/v1',
            query_per_second=1,
            max_seq_len=4096,
            retry=10
        ),
        tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),
    'qwen2-vl-7b-instruction_vlm_tool_stepbystep': dict(
        abbr='qwen2-vl-7b-instruction_vlm_tool_stepbystep',
        type=LagentAgentVisual,
        agent_type=ReAct,
        max_turn=6,
        llm=dict(
            type=OpenAIVisual,
            path='Qwen2-VL-7B-Instruct',
            key='EMPTY', # put your key here
            openai_api_base='http://222.29.51.128:12587/v1',
            query_per_second=1,
            max_seq_len=4096,
            retry=10
        ),
        tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),
    'qwen2-vl-2b-instruction_vlm_tool_stepbystep': dict(
        abbr='qwen2-vl-2b-instruction_vlm_tool_stepbystep',
        type=LagentAgentVisual,
        agent_type=ReAct,
        max_turn=6,
        llm=dict(
            type=OpenAIVisual,
            path='Qwen2-VL-2B-Instruct',
            key='EMPTY', # put your key here
            openai_api_base='http://222.29.51.128:12582/v1',
            query_per_second=1,
            max_seq_len=4096,
            retry=10
        ),
        tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),
    'llava-v1.5-7b_vlm_tool_stepbystep': dict(
        abbr='llava-v1.5-7b_vlm_tool_stepbystep',
        type=LagentAgentVisual,
        agent_type=ReAct,
        max_turn=6,
        llm=dict(
            type=OpenAIVisual,
            path='llava-v1.5-7b',
            key='EMPTY', # put your key here
            openai_api_base='http://222.29.51.128:12585/v1',
            query_per_second=1,
            max_seq_len=4096,
            stop='<|eot_id|>',
        ),
        tool_meta='data/gta_dataset/toolmeta.json',
        # tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),
    'llava-ft-4000_vlm_tool_stepbystep': dict(
        abbr='llava-ft-4000_vlm_tool_stepbystep',
        type=LagentAgentVisualLocal,
        agent_type=ReAct,
        max_turn=6,
        llm=dict(
            type=OpenAIVisual,
            path='llava-ft-4000',
            key='EMPTY', # put your key here
            openai_api_base='http://222.29.51.128:12587/v1',
            query_per_second=1,
            max_seq_len=4096,
            stop='<|eot_id|>',
        ),
        tool_meta='data/gta_dataset/toolmeta.json',
        # tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),
    

    ######################### VLM / LLM #########################
    
    'chatgpt-4o-latest_llm_tool_stepbystep': dict(
        abbr='chatgpt-4o-latest_llm_tool_stepbystep',
        type=LagentAgent,
        agent_type=ReAct,
        max_turn=6,
        llm=dict(
            type=OpenAI,
            path='chatgpt-4o-latest',
            key=api_key, # put your key here
            openai_api_base='https://29qg.com/v1/chat/completions',
            query_per_second=1,
            max_seq_len=4096,
            retry=10
        ),
        # tool_server='http://222.29.51.126:16181', # end-to-end
        tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),
    'claude-3-5-sonnet_llm_tool_stepbystep': dict(
        abbr='claude-3-5-sonnet_llm_tool_sbs',
        type=LagentAgent,
        agent_type=ReAct,
        max_turn=6,
        llm=dict(
            type=OpenAI,
            path='claude-3-5-sonnet-20240620',
            key=api_key, # put your key here
            openai_api_base='https://29qg.com/v1/chat/completions',
            query_per_second=1,
            max_seq_len=4096,
            retry=10
        ),
        # tool_server='http://222.29.51.126:16181', # end-to-end
        tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),
    'gpt-4o_llm_tool_stepbystep': dict(
        abbr='gpt-4o_llm_tool_stepbystep',
        type=LagentAgent,
        agent_type=ReAct,
        max_turn=6,
        llm=dict(
            type=OpenAI,
            path='gpt-4o',
            key=api_key, # put your key here
            openai_api_base='https://29qg.com/v1/chat/completions',
            query_per_second=1,
            max_seq_len=4096,
            retry=10
        ),
        # tool_server='http://222.29.51.126:16181', # end-to-end
        tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),
    'gpt-3.5-turbo_llm_tool_stepbystep': dict(
        abbr='gpt-3.5-turbo_llm_tool_stepbystep',
        type=LagentAgent,
        agent_type=ReAct,
        max_turn=6,
        llm=dict(
            type=OpenAI,
            path='gpt-3.5-turbo',
            key=api_key, # put your key here
            openai_api_base='https://29qg.com/v1/chat/completions',
            query_per_second=1,
            max_seq_len=4096,
            retry=10
        ),
        # tool_server='http://222.29.51.126:16181', # end-to-end
        tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),
    'llava-ft-nocaption_llm_tool_stepbystep': dict(
        abbr='llava-ft-nocaption_llm_tool',
        type=LagentAgent,
        agent_type=ReAct,
        max_turn=6,
        llm=dict(
            type=OpenAI,
            path='llava-ft-nocaption',
            key='EMPTY', # put your key here
            openai_api_base='http://222.29.51.128:12587/v1/chat/completions',
            query_per_second=1,
            max_seq_len=3072,
            stop='<|eot_id|>',
        ),
        # tool_server='http://222.29.51.126:16181', # end-to-end
        tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),


    'Meta-Llama-3-8B-Instruct-ft-4000_llm_tool_stepbystep': dict(
        abbr='Meta-Llama-3-8B-Instruct-ft-4000_llm_tool_stepbystep',
        type=LagentAgent,
        agent_type=ReAct,
        max_turn=6,
        llm=dict(
            type=OpenAI,
            path='Meta-Llama-3-8B-Instruct-ft-4000',
            key='EMPTY',
            openai_api_base='http://222.29.51.126:xxxxx/v1/chat/completions',
            query_per_second=1,
            max_seq_len=4096,
            stop='<|eot_id|>',
        ),
        tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),
    'Meta-Llama-3-8B-Instruct_llm_tool_stepbystep': dict(
        abbr='Meta-Llama-3-8B-Instruct_llm_tool_stepbystep',
        type=LagentAgent,
        agent_type=ReAct,
        max_turn=6,
        llm=dict(
            type=OpenAI,
            path='Meta-Llama-3-8B-Instruct',
            key='EMPTY',
            openai_api_base='http://222.29.51.126:12582/v1/chat/completions',
            query_per_second=1,
            max_seq_len=4096,
            stop='<|eot_id|>',
        ),
        tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),
    'llava-ft-4000_llm_tool_stepbystep': dict(
        abbr='llava-ft-4000_llm_tool_stepbystep',
        type=LagentAgent,
        agent_type=ReAct,
        max_turn=6,
        llm=dict(
            type=OpenAI,
            path='llava-ft-4000',
            key='EMPTY', # put your key here
            openai_api_base='http://222.29.51.128:12587/v1/chat/completions',
            query_per_second=1,
            max_seq_len=4096,
            stop='<|eot_id|>',
        ),
        # tool_server='http://222.29.51.126:16181', # end-to-end
        tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),

    'llava-v1.5-7b_llm_tool_stepbystep': dict(
        abbr='llava-v1.5-7b_llm_tool_stepbystep',
        type=LagentAgent,
        agent_type=ReAct,
        max_turn=6,
        llm=dict(
            type=OpenAI,
            path='llava-v1.5-7b',
            key='EMPTY', # put your key here
            openai_api_base='http://222.29.51.128:12585/v1/chat/completions',
            query_per_second=1,
            max_seq_len=4096,
            stop='<|eot_id|>',
        ),
        # tool_server='http://222.29.51.126:16181', # end-to-end
        tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),
    'qwen2-vl-7b-instruction_llm_tool_stepbystep': dict(
        abbr='qwen2-vl-7b-instruction_llm_tool_stepbystep',
        type=LagentAgent,
        agent_type=ReAct,
        max_turn=6,
        llm=dict(
            type=OpenAI,
            path='Qwen2-VL-7B-Instruct',
            key='EMPTY', # put your key here
            openai_api_base='http://222.29.51.128:12587/v1/chat/completions',
            query_per_second=1,
            max_seq_len=4096,
            retry=10
        ),
        tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),
    'qwen2-vl-2b-instruction_llm_tool_stepbystep': dict(
        abbr='qwen2-vl-2b-instruction_llm_tool_stepbystep',
        type=LagentAgent,
        agent_type=ReAct,
        max_turn=6,
        llm=dict(
            type=OpenAI,
            path='Qwen2-VL-2B-Instruct',
            key='EMPTY', # put your key here
            openai_api_base='http://222.29.51.128:12582/v1/chat/completions',
            query_per_second=1,
            max_seq_len=4096,
            retry=10
        ),
        tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),
    'qwen2-7b-instruction_llm_tool_stepbystep': dict(
        abbr='qwen2-7b-instruction_llm_tool_stepbystep',
        type=LagentAgent,
        agent_type=ReAct,
        max_turn=6,
        llm=dict(
            type=OpenAI,
            path='Qwen2-7B-Instruct',
            key='EMPTY', # put your key here
            openai_api_base='http://222.29.51.128:12581/v1/chat/completions',
            query_per_second=1,
            max_seq_len=4096,
            retry=10
        ),
        tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),
    'qwen2-1.5b-instruction_llm_tool_stepbystep': dict(
        abbr='qwen2-1.5b-instruction_llm_tool_stepbystep',
        type=LagentAgent,
        agent_type=ReAct,
        max_turn=6,
        llm=dict(
            type=OpenAI,
            path='Qwen2-1.5B-Instruct',
            key='EMPTY', # put your key here
            openai_api_base='http://222.29.51.128:12582/v1/chat/completions',
            query_per_second=1,
            max_seq_len=4096,
            retry=10
        ),
        tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),
    'gemma-2b-it_llm_tool_stepbystep': dict(
        abbr='gemma-2b-it_llm_tool_stepbystep',
        type=LagentAgent,
        agent_type=ReAct,
        max_turn=6,
        llm=dict(
            type=OpenAI,
            path='gemma-2b-it',
            key='EMPTY', # put your key here
            openai_api_base='http://222.29.51.128:12582/v1/chat/completions',
            query_per_second=1,
            max_seq_len=4096,
            retry=10
        ),
        tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),

}


infer = dict(
    partitioner=dict(type=SizePartitioner, max_task_size=4000, gen_task_coef=1),
    runner=dict(type=LocalRunner, task=dict(type=OpenICLInferTask)),
)
