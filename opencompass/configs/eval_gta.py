from lagent.agents import ReAct
from mmengine.config import read_base

from opencompass.models import OpenAI, Qwen, Gemini, OpenAIVisual, OpenAIVisualDummy
from opencompass.models.lagent import LagentAgent, LagentAgentVisual, LagentAgentVisualLocal
from opencompass.partitioners import SizePartitioner
from opencompass.runners import LocalRunner
from opencompass.tasks import OpenICLInferTask

with read_base():
    from .datasets.gta_bench import gta_bench_datasets as datasets

import os
api_key = os.getenv('OPENAI_API_KEY')

models = {
    'chatgpt-4o-latest_vlm_gta': dict(
        abbr='chatgpt-4o-latest_gta',
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
        tool_server='http://128.32.162.186:16181', # end-to-end
        # tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),

    ######################### Dummy VLM / Tool VLM #########################
    
    'qwen2-vl-2b-gaia-instruct-gta': dict(
        abbr='qwen2-vl-2b-gaia-instruct-gta',
        type=LagentAgentVisual,
        agent_type=ReAct,
        max_turn=8,
        llm=dict(
            type=OpenAIVisual,
            path='Qwen2-VL-2B-Instruct',
            key='EMPTY', # put your key here
            openai_api_base='http://128.32.162.179:12581/v1',
            query_per_second=1,
            max_seq_len=4096,
        ),
        tool_server='http://128.32.162.179:16181', # end-to-end
        batch_size=8,
    ),
    
    'qwen2-vl-2b-mm-instruct-gta': dict(
        abbr='qwen2-vl-2b-mm-instruct-gta',
        type=LagentAgentVisual,
        agent_type=ReAct,
        max_turn=8,
        llm=dict(
            type=OpenAIVisual,
            path='Qwen2-VL-2B-Instruct',
            key='EMPTY', # put your key here
            openai_api_base='http://128.32.162.179:12582/v1',
            query_per_second=1,
            max_seq_len=4096,
        ),
        tool_server='http://128.32.162.179:16181', # end-to-end
        batch_size=8,
    ),
    
}


infer = dict(
    partitioner=dict(type=SizePartitioner, max_task_size=4000, gen_task_coef=1),
    runner=dict(type=LocalRunner, task=dict(type=OpenICLInferTask)),
)
