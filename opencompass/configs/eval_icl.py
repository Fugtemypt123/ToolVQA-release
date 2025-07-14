from lagent.agents import ReAct
from mmengine.config import read_base

from opencompass.models import OpenAI, Qwen, Gemini, OpenAIVisual, OpenAIVisualDummy, OpenAIICL
from opencompass.models.lagent import LagentAgent, LagentAgentVisual, LagentAgentVisualLocal
from opencompass.partitioners import SizePartitioner
from opencompass.runners import LocalRunner
from opencompass.tasks import OpenICLInferTask

with read_base():
    from .datasets.gta_bench import gta_bench_datasets as datasets

import os
api_key = os.getenv('OPENAI_API_KEY')

models = {
    'llama3-8b-icl': dict(
        abbr='llama3-8b-icl',
        type=LagentAgent,
        agent_type=ReAct,
        max_turn=6,
        llm=dict(
            type=OpenAIICL,
            path='Meta-Llama-3-8B-Instruct',
            key='EMPTY',
            # openai_api_base='http://10.140.1.17:12580/v1/chat/completions',
            # openai_api_base='http://222.29.51.126:12580/v1/chat/completions',
            openai_api_base='http://222.29.51.126:12581/v1/chat/completions',
            query_per_second=1,
            max_seq_len=4096,
            stop='<|eot_id|>',
        ),
    #  tool_server='http://10.140.0.138:16181',
        # tool_server='http://222.29.51.126:16181', # end-to-end
        tool_server='http://222.29.51.126:16181', # end-to-end
        # tool_meta='data/gta_dataset/toolmeta.json', # step by step
        batch_size=8,
    ),
    ######################### VLM / LLM #########################

    'chatgpt-4o-latest-icl': dict(
        abbr='chatgpt-4o-latest-icl',
        type=LagentAgent,
        agent_type=ReAct,
        max_turn=6,
        llm=dict(
            type=OpenAI,
            path='chatgpt-4o-latest',
            key=api_key, # put your key here
            openai_api_base='https://api.openai.com/v1/chat/completions',
            query_per_second=1,
            max_seq_len=4096,
            retry=10
        ),
        tool_server='http://128.32.162.179:16181',
        # tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),

    'gpt-3.5-turbo-icl': dict(
        abbr='gpt-3.5-turbo-icl',
        type=LagentAgent,
        agent_type=ReAct,
        max_turn=6,
        llm=dict(
            type=OpenAIICL,
            path='gpt-3.5-turbo',
            key=api_key, # put your key here
            openai_api_base='https://29qg.com/v1/chat/completions',
            query_per_second=1,
            max_seq_len=4096,
            retry=10
        ),
        tool_server='http://222.29.51.126:16181',
        # tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),
}


infer = dict(
    partitioner=dict(type=SizePartitioner, max_task_size=4000, gen_task_coef=1),
    runner=dict(type=LocalRunner, task=dict(type=OpenICLInferTask)),
)
