from lagent.agents import ReAct
from mmengine.config import read_base

from opencompass.models import OpenAI, Qwen, Gemini, OpenAIVisual, OpenAIVisualDummy
from opencompass.models.lagent import LagentAgent, LagentAgentVisual, LagentAgentVisualLocal
from opencompass.partitioners import SizePartitioner
from opencompass.runners import LocalRunner
from opencompass.tasks import OpenICLInferTask

with read_base():
    from .datasets.gta_bench_tallyqa import gta_bench_datasets as datasets

import os
api_key = os.getenv('OPENAI_API_KEY')

models = {
    'chatgpt-4o-latest_vlm_tallyqa': dict(
        abbr='chatgpt-4o-latest_tallyqa',
        type=LagentAgentVisual,
        agent_type=ReAct,
        max_turn=1,
        llm=dict(
            type=OpenAIVisualDummy,
            path='chatgpt-4o-latest',
            key=api_key, # put your key here
            openai_api_base='https://29qg.com/v1',
            query_per_second=1,
            max_seq_len=4096,
            retry=10
        ),
        tool_server='http://222.29.51.126:16181', # end-to-end
        # tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),

    'llava-v1.5-7b_vlm_tallyqa': dict(
        abbr='llava-v1.5-7b_vlm_tallyqa',
        type=LagentAgentVisual,
        agent_type=ReAct,
        max_turn=1,
        llm=dict(
            type=OpenAIVisualDummy,
            path='llava-v1.5-7b',
            key='EMPTY', 
            openai_api_base='http://222.29.51.126:12580/v1',
            query_per_second=1,
            max_seq_len=4096,
            stop='<|eot_id|>',
        ),
        tool_server='http://222.29.51.126:16181', # end-to-end
        # tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),

    ######################### Dummy VLM / Tool VLM #########################
    
    'llava-ft-4000_vlm_tool_tallyqa': dict(
        abbr='llava-ft-4000_vlm_tool_tallyqa',
        type=LagentAgentVisualLocal,
        agent_type=ReAct,
        max_turn=4,
        llm=dict(
            type=OpenAIVisual,
            path='llava-ft-4000',
            key='EMPTY', # put your key here
            openai_api_base='http://222.29.51.126:12581/v1',
            query_per_second=1,
            max_seq_len=3072,
            stop='<|eot_id|>',
        ),
        tool_server='http://222.29.51.126:16181', # end-to-end
        batch_size=8,
    ),

    ######################### VLM / LLM #########################
    
    'Meta-Llama-3-8B-Instruct_llm_tool_tallyqa': dict(
        abbr='Meta-Llama-3-8B-Instruct_llm_tool_tallyqa',
        type=LagentAgent,
        agent_type=ReAct,
        max_turn=6,
        llm=dict(
            type=OpenAI,
            path='Meta-Llama-3-8B-Instruct',
            key='EMPTY',
            openai_api_base='http://222.29.51.126:12581/v1/chat/completions',
            query_per_second=1,
            max_seq_len=4096,
            stop='<|eot_id|>',
        ),
        tool_server='http://222.29.51.126:16181', # end-to-end
        batch_size=8,
    ),
    'llama-ft-1000_llm_tool_tallyqa': dict(
        abbr='llama-ft-1000_llm_tool_tallyqa',
        type=LagentAgent,
        agent_type=ReAct,
        max_turn=6,
        llm=dict(
            type=OpenAI,
            path='llama-ft-1000',
            key='EMPTY',
            openai_api_base='http://222.29.51.126:12580/v1/chat/completions',
            query_per_second=1,
            max_seq_len=3072,
            stop='<|eot_id|>',
        ),
        tool_server='http://222.29.51.126:16181', # end-to-end
        batch_size=8,
    ),
    'llava-llama-3-8b-v1_1-transformers_llm_tool_tallyqa': dict(
        abbr='llava-llama-3-8b-v1_1-transformers_llm_tool_tallyqa',
        type=LagentAgent,
        agent_type=ReAct,
        max_turn=6,
        llm=dict(
            type=OpenAI,
            path='llava-llama-3-8b-v1_1-transformers',
            key='EMPTY', # put your key here
            openai_api_base='http://222.29.51.126:12580/v1/chat/completions',
            query_per_second=1,
            max_seq_len=4096,
            stop='<|eot_id|>',
        ),
        tool_server='http://222.29.51.126:16181', # end-to-end
        # tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),
    'llava-8b-ft-qlora-8000_llm_tool_tallyqa': dict(
        abbr='llava-8b-ft-qlora-8000_llm_tool_tallyqa',
        type=LagentAgent,
        agent_type=ReAct,
        max_turn=6,
        llm=dict(
            type=OpenAI,
            path='llava-8b-ft-qlora-8000',
            key='EMPTY', # put your key here
            openai_api_base='http://222.29.51.126:12582/v1/chat/completions',
            query_per_second=1,
            max_seq_len=4096,
            stop='<|eot_id|>',
        ),
        tool_server='http://222.29.51.126:16181', # end-to-end
        # tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),
    'gpt-3.5-turbo_llm_tool_tallyqa': dict(
        abbr='gpt-3.5-turbo_llm_tool_tallyqa',
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
        tool_server='http://222.29.51.126:16181', # end-to-end
        # tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),

}


infer = dict(
    partitioner=dict(type=SizePartitioner, max_task_size=4000, gen_task_coef=1),
    runner=dict(type=LocalRunner, task=dict(type=OpenICLInferTask)),
)
