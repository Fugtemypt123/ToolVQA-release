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
    'llava-ft-4000-ablation-singlehop_vlm': dict(
        abbr='llava-ft-4000-ablation-singlehop_vlm',
        type=LagentAgentVisualLocal,
        agent_type=ReAct,
        max_turn=1,
        llm=dict(
            type=OpenAIVisualDummy,
            path='llava-ft-4000-ablation-singlehop',
            key='EMPTY', # put your key here
            openai_api_base='http://222.29.51.126:12581/v1',
            query_per_second=1,
            max_seq_len=3072,
            stop='<|eot_id|>',
        ),
        tool_server='http://222.29.51.126:16181', # end-to-end
        # tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),
    'chatgpt-4o-latest_vlm': dict(
        abbr='chatgpt-4o-latest_vlm',
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
        tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),
    'claude-3-5-sonnet_vlm': dict(
        abbr='claude-3-5-sonnet_vlm',
        type=LagentAgentVisual,
        agent_type=ReAct,
        max_turn=1,
        llm=dict(
            type=OpenAIVisualDummy,
            path='claude-3-5-sonnet-20240620',
            key=api_key, # put your key here
            openai_api_base='https://29qg.com/v1',
            query_per_second=1,
            max_seq_len=4096,
            retry=10
        ),
        tool_server='http://222.29.51.126:16181', # end-to-end
        tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),
    'gpt-4o_vlm': dict(
        abbr='gpt-4o_vlm',
        type=LagentAgentVisual,
        agent_type=ReAct,
        max_turn=1,
        llm=dict(
            type=OpenAIVisualDummy,
            path='gpt-4o',
            key=api_key, # put your key here
            openai_api_base='https://29qg.com/v1',
            query_per_second=1,
            max_seq_len=4096,
            retry=10
        ),
        tool_server='http://222.29.51.126:16181', # end-to-end
        tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),
    'qwen2-vl-2b-instruct_vlm': dict(
        abbr='qwen2-vl-2b-instruct_vlm',
        type=LagentAgentVisualLocal,
        agent_type=ReAct,
        max_turn=1,
        llm=dict(
            type=OpenAIVisualDummy,
            path='qwen2-vl-2b-instruct',
            key='EMPTY', # put your key here
            openai_api_base='http://222.29.51.126:12580/v1',
            query_per_second=1,
            max_seq_len=4096,
            stop='<|im_end|>',
        ),
        tool_server='http://222.29.51.126:16181', # end-to-end
        # tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),
    'Qwen2-VL-7B-Instruct_vlm': dict(
        abbr='Qwen2-VL-7B-Instruct_vlm',
        type=LagentAgentVisualLocal,
        agent_type=ReAct,
        max_turn=1,
        llm=dict(
            type=OpenAIVisualDummy,
            path='Qwen2-VL-7B-Instruct',
            key='EMPTY', # put your key here
            openai_api_base='http://222.29.51.126:12581/v1',
            query_per_second=1,
            max_seq_len=4096,
            stop='<|im_end|>',
        ),
        tool_server='http://222.29.51.126:16181', # end-to-end
        # tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),
    'llava-llama-3-8b-v1_1-transformers_vlm': dict(
        abbr='llava-llama-3-8b-v1_1-transformers_vlm',
        type=LagentAgentVisualLocal,
        agent_type=ReAct,
        max_turn=1,
        llm=dict(
            type=OpenAIVisualDummy,
            path='llava-llama-3-8b-v1_1-transformers',
            key='EMPTY', # put your key here
            openai_api_base='http://222.29.51.126:12580/v1',
            query_per_second=1,
            max_seq_len=4096,
            stop='<|eot_id|>',
        ),
        tool_server='http://222.29.51.126:16181', # end-to-end
        # tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),
    'llava-8b-ft-qlora-4864_vlm': dict(
        abbr='llava-8b-ft-qlora-4864_vlm',
        type=LagentAgentVisualLocal,
        agent_type=ReAct,
        max_turn=1,
        llm=dict(
            type=OpenAIVisualDummy,
            path='llava-8b-ft-qlora-4864',
            key='EMPTY', # put your key here
            openai_api_base='http://222.29.51.126:12581/v1',
            query_per_second=1,
            max_seq_len=4096,
            stop='<|eot_id|>',
        ),
        tool_server='http://222.29.51.126:16181', # end-to-end
        # tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),
    'llava-8b-ft-qlora-8000_vlm': dict(
        abbr='llava-8b-ft-qlora-8000_vlm',
        type=LagentAgentVisualLocal,
        agent_type=ReAct,
        max_turn=1,
        llm=dict(
            type=OpenAIVisualDummy,
            path='llava-8b-ft-qlora-8000',
            key='EMPTY', # put your key here
            openai_api_base='http://222.29.51.126:12582/v1',
            query_per_second=1,
            max_seq_len=4096,
            stop='<|eot_id|>',
        ),
        tool_server='http://222.29.51.126:16181', # end-to-end
        # tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),

    ######################### Dummy VLM / Tool VLM #########################
    
    'chatgpt-4o-latest_vlm_tool': dict(
        abbr='chatgpt-4o-latest_vlm_tool',
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
        tool_server='http://222.29.51.126:16181', # end-to-end
        tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),
    'claude-3-5-sonnet_vlm_tool': dict(
        abbr='claude-3-5-sonnet_vlm_tool',
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
        ),
        tool_server='http://222.29.51.126:16181', # end-to-end
        tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),
    'gpt-4o_vlm_tool': dict(
        abbr='gpt-4o_vlm_tool',
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
        tool_server='http://222.29.51.126:16181', # end-to-end
        tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),
    'qwen2-vl-2b-instruct_vlm_tool': dict(
        abbr='qwen2-vl-2b-instruct_vlm_tool',
        type=LagentAgentVisualLocal,
        agent_type=ReAct,
        max_turn=6,
        llm=dict(
            type=OpenAIVisual,
            path='qwen2-vl-2b-instruct',
            key='EMPTY', # put your key here
            openai_api_base='http://222.29.51.126:12580/v1',
            query_per_second=1,
            max_seq_len=4096,
            stop='<|im_end|>',
        ),
        tool_server='http://222.29.51.126:16181', # end-to-end
        # tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),
    'Qwen2-VL-7B-Instruct_vlm_tool': dict(
        abbr='Qwen2-VL-7B-Instruct_vlm_tool',
        type=LagentAgentVisualLocal,
        agent_type=ReAct,
        max_turn=5,
        llm=dict(
            type=OpenAIVisual,
            path='Qwen2-VL-7B-Instruct',
            key='EMPTY', # put your key here
            openai_api_base='http://222.29.51.126:12581/v1',
            query_per_second=1,
            max_seq_len=4096,
            stop='<|im_end|>',
        ),
        tool_server='http://222.29.51.126:16181', # end-to-end
        # tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),
    'llava-llama-3-8b-v1_1-transformers_vlm_tool': dict(
        abbr='llava-llama-3-8b-v1_1-transformers_vlm_tool',
        type=LagentAgentVisualLocal,
        agent_type=ReAct,
        max_turn=6,
        llm=dict(
            type=OpenAIVisual,
            path='llava-llama-3-8b-v1_1-transformers',
            key='EMPTY', # put your key here
            openai_api_base='http://222.29.51.126:12580/v1',
            query_per_second=1,
            max_seq_len=4096,
            stop='<|eot_id|>',
        ),
        tool_server='http://222.29.51.126:16181', # end-to-end
        # tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),
    'llava-8b-ft-qlora-4864_vlm_tool': dict(
        abbr='llava-8b-ft-qlora-4864_vlm_tool',
        type=LagentAgentVisualLocal,
        agent_type=ReAct,
        max_turn=6,
        llm=dict(
            type=OpenAIVisual,
            path='llava-8b-ft-qlora-4864',
            key='EMPTY', # put your key here
            openai_api_base='http://222.29.51.126:12581/v1',
            query_per_second=1,
            max_seq_len=4096,
            stop='<|eot_id|>',
        ),
        tool_server='http://222.29.51.126:16181', # end-to-end
        # tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),
    'llava-8b-ft-qlora-8000_vlm_tool': dict(
        abbr='llava-8b-ft-qlora-8000_vlm_tool',
        type=LagentAgentVisualLocal,
        agent_type=ReAct,
        max_turn=6,
        llm=dict(
            type=OpenAIVisual,
            path='llava-8b-ft-qlora-8000',
            key='EMPTY', # put your key here
            openai_api_base='http://222.29.51.126:12582/v1',
            query_per_second=1,
            max_seq_len=2048,
            stop='<|eot_id|>',
        ),
        tool_server='http://222.29.51.126:16181', # end-to-end
        # tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),
    'llava-ft-4000_vlm_tool': dict(
        abbr='llava-ft-4000_vlm_tool',
        type=LagentAgentVisualLocal,
        agent_type=ReAct,
        max_turn=6,
        llm=dict(
            type=OpenAIVisual,
            path='llava-ft-4000',
            key='EMPTY', # put your key here
            openai_api_base='http://222.29.51.128:12586/v1',
            query_per_second=1,
            max_seq_len=3072,
            stop='<|eot_id|>',
        ),
        tool_server='http://222.29.51.126:16181', # end-to-end
        # tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),
    'llava-ft-100_vlm_tool': dict(
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
        tool_server='http://222.29.51.126:16181', # end-to-end
        # tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),
    'llava-ft-1000_vlm_tool': dict(
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
        tool_server='http://222.29.51.126:16181', # end-to-end
        # tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),
    'llava-ft-53760_vlm_tool': dict(
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
        tool_server='http://222.29.51.126:16181', # end-to-end
        # tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),
    'llava-ft-4000-ablation-1000_vlm_tool': dict(
        abbr='llava-ft-4000-ablation-1000_vlm_tool',
        type=LagentAgentVisualLocal,
        agent_type=ReAct,
        max_turn=6,
        llm=dict(
            type=OpenAIVisual,
            path='llava-ft-4000-ablation-1000',
            key='EMPTY', # put your key here
            openai_api_base='http://222.29.51.126:12581/v1',
            query_per_second=1,
            max_seq_len=3072,
            stop='<|eot_id|>',
        ),
        tool_server='http://222.29.51.126:16181', # end-to-end
        # tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),
    'llava-ft-4000-ablation-5000_vlm_tool': dict(
        abbr='llava-ft-4000-ablation-5000_vlm_tool',
        type=LagentAgentVisualLocal,
        agent_type=ReAct,
        max_turn=6,
        llm=dict(
            type=OpenAIVisual,
            path='llava-ft-4000-ablation-5000',
            key='EMPTY', # put your key here
            openai_api_base='http://222.29.51.126:12582/v1',
            query_per_second=1,
            max_seq_len=3072,
            stop='<|eot_id|>',
        ),
        tool_server='http://222.29.51.126:16181', # end-to-end
        # tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),
    'llava-ft-nocaption_vlm_tool': dict(
        abbr='llava-ft-nocaption_vlm_tool',
        type=LagentAgentVisualLocal,
        agent_type=ReAct,
        max_turn=6,
        llm=dict(
            type=OpenAIVisual,
            path='llava-ft-nocaption',
            key='EMPTY', # put your key here
            openai_api_base='http://222.29.51.128:12586/v1',
            query_per_second=1,
            max_seq_len=3072,
            stop='<|eot_id|>',
        ),
        tool_server='http://222.29.51.126:16181', # end-to-end
        # tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),
    'llava-ft-4000-ablation-singlehop_vlm_tool': dict(
        abbr='llava-ft-4000-ablation-singlehop_vlm_tool',
        type=LagentAgentVisualLocal,
        agent_type=ReAct,
        max_turn=6,
        llm=dict(
            type=OpenAIVisual,
            path='llava-ft-4000-ablation-singlehop',
            key='EMPTY', # put your key here
            openai_api_base='http://222.29.51.126:12581/v1',
            query_per_second=1,
            max_seq_len=3072,
            stop='<|eot_id|>',
        ),
        tool_server='http://222.29.51.126:16181', # end-to-end
        # tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),

    ######################### VLM / LLM #########################

    'gpt-3.5-turbo_llm_tool_icl': dict(
        abbr='gpt-3.5-turbo_llm_tool_icl',
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
    'gpt-3.5-turbo_llm_tool': dict(
        abbr='gpt-3.5-turbo_llm_tool',
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
        tool_server='http://222.29.51.126:16181',
        # tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),
    'chatgpt-4o-latest_llm_tool': dict(
        abbr='chatgpt-4o-latest_llm_tool',
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
        tool_server='http://222.29.51.126:16181', # end-to-end
        # tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),
    'chatgpt-4o-latest_llm_tool_sbs': dict(
        abbr='chatgpt-4o-latest_llm_tool',
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
    'claude-3-5-sonnet_llm_tool': dict(
        abbr='claude-3-5-sonnet_llm_tool',
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
        tool_server='http://222.29.51.126:16181', # end-to-end
        # tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),
    'claude-3-5-sonnet_llm_tool_sbs': dict(
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
    'gpt-4-1106_llm_tool': dict(
        abbr='gpt-4-1106_llm_tool',
        type=LagentAgent,
        agent_type=ReAct,
        max_turn=6,
        llm=dict(
            type=OpenAI,
            path='gpt-4-1106-preview',
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
    'gpt-4o_llm_tool': dict(
        abbr='gpt-4o_llm_tool',
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
        tool_server='http://222.29.51.126:16181', # end-to-end
        # tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),
    'gemma-2b-it_llm_tool': dict(
        abbr='gemma-2b-it_llm_tool',
        type=LagentAgent,
        agent_type=ReAct,
        max_turn=6,
        llm=dict(
            type=OpenAI,
            path='gemma-2b-it',
            key='EMPTY', # put your key here
            openai_api_base='http://222.29.51.126:12580/v1/chat/completions',
            query_per_second=1,
            max_seq_len=4096,
            stop='<|im_end|>',
        ),
        tool_server='http://222.29.51.126:16181', # end-to-end
        # tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),
    'qwen2-vl-2b-instruct_llm_tool': dict(
        abbr='qwen2-vl-2b-instruct_llm_tool',
        type=LagentAgent,
        agent_type=ReAct,
        max_turn=6,
        llm=dict(
            type=OpenAI,
            path='qwen2-vl-2b-instruct',
            key='EMPTY',
            openai_api_base='http://222.29.51.126:12580/v1/chat/completions',
            query_per_second=1,
            max_seq_len=4096,
            stop='<|im_end|>',
        ),
        tool_server='http://222.29.51.126:16181', # end-to-end
        batch_size=8,
    ),
    'qwen2-1.5b-instruct_llm_tool': dict(
        abbr='qwen2-1.5b-instruct_llm_tool',
        type=LagentAgent,
        agent_type=ReAct,
        max_turn=6,
        llm=dict(
            type=OpenAI,
            path='qwen2-1.5b-instruct',
            key='EMPTY',
            # openai_api_base='http://10.140.1.17:12580/v1/chat/completions',
            # openai_api_base='http://222.29.51.126:12580/v1/chat/completions',
            openai_api_base='http://222.29.51.126:12581/v1/chat/completions',
            query_per_second=1,
            max_seq_len=4096,
            stop='<|im_end|>',
        ),
    #  tool_server='http://10.140.0.138:16181',
        # tool_server='http://222.29.51.126:16181', # end-to-end
        tool_server='http://222.29.51.126:16181', # end-to-end
        # tool_meta='data/gta_dataset/toolmeta.json', # step by step
        batch_size=8,
    ),
    'Qwen2-VL-7B-Instruct_llm_tool': dict(
        abbr='Qwen2-VL-7B-Instruct_llm_tool',
        type=LagentAgent,
        agent_type=ReAct,
        max_turn=5,
        llm=dict(
            type=OpenAI,
            path='Qwen2-VL-7B-Instruct',
            key='EMPTY',
            # openai_api_base='http://10.140.1.17:12580/v1/chat/completions',
            # openai_api_base='http://222.29.51.126:12580/v1/chat/completions',
            openai_api_base='http://222.29.51.126:12581/v1/chat/completions',
            query_per_second=1,
            max_seq_len=2048,
            stop='<|im_end|>',
        ),
    #  tool_server='http://10.140.0.138:16181',
        # tool_server='http://222.29.51.126:16181', # end-to-end
        tool_server='http://222.29.51.126:16181', # end-to-end
        # tool_meta='data/gta_dataset/toolmeta.json', # step by step
        batch_size=8,
    ),
    'Qwen2-7B-Instruct_llm_tool': dict(
        abbr='Qwen2-7B-Instruct_llm_tool',
        type=LagentAgent,
        agent_type=ReAct,
        max_turn=6,
        llm=dict(
            type=OpenAI,
            path='Qwen2-7B-Instruct',
            key='EMPTY',
            # openai_api_base='http://10.140.1.17:12580/v1/chat/completions',
            # openai_api_base='http://222.29.51.126:12580/v1/chat/completions',
            openai_api_base='http://222.29.51.126:12581/v1/chat/completions',
            query_per_second=1,
            max_seq_len=4096,
            stop='<|im_end|>',
        ),
    #  tool_server='http://10.140.0.138:16181',
        # tool_server='http://222.29.51.126:16181', # end-to-end
        tool_server='http://222.29.51.126:16181', # end-to-end
        # tool_meta='data/gta_dataset/toolmeta.json', # step by step
        batch_size=8,
    ),
    'Meta-Llama-3-8B-Instruct_llm_tool': dict(
        abbr='Meta-Llama-3-8B-Instruct_llm_tool',
        type=LagentAgent,
        agent_type=ReAct,
        max_turn=6,
        llm=dict(
            type=OpenAI,
            path='Meta-Llama-3-8B-Instruct',
            key='EMPTY',
            # openai_api_base='http://10.140.1.17:12580/v1/chat/completions',
            # openai_api_base='http://222.29.51.126:12580/v1/chat/completions',
            openai_api_base='http://222.29.51.126:12580/v1/chat/completions',
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
    'Meta-Llama-3-8B-Instruct-ft-8000_llm_tool': dict(
        abbr='Meta-Llama-3-8B-Instruct-ft-8000_llm_tool',
        type=LagentAgent,
        agent_type=ReAct,
        max_turn=6,
        llm=dict(
            type=OpenAI,
            path='Meta-Llama-3-8B-Instruct-ft-8000',
            key='EMPTY',
            openai_api_base='http://222.29.51.126:12581/v1/chat/completions',
            query_per_second=1,
            max_seq_len=4096,
            stop='<|eot_id|>',
        ),
        tool_server='http://222.29.51.126:16182', # end-to-end
        batch_size=8,
    ),
    'llava-llama-3-8b-v1_1-transformers_llm_tool': dict(
        abbr='llava-llama-3-8b-v1_1-transformers_llm_tool',
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
    'llava-8b-ft-qlora-4864_llm_tool': dict(
        abbr='llava-8b-ft-qlora-4864_llm_tool',
        type=LagentAgent,
        agent_type=ReAct,
        max_turn=6,
        llm=dict(
            type=OpenAI,
            path='llava-8b-ft-qlora-4864',
            key='EMPTY', # put your key here
            openai_api_base='http://222.29.51.126:12581/v1/chat/completions',
            query_per_second=1,
            max_seq_len=4096,
            stop='<|eot_id|>',
        ),
        tool_server='http://222.29.51.126:16181', # end-to-end
        # tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),
    'llava-8b-ft-qlora-8000_llm_tool': dict(
        abbr='llava-8b-ft-qlora-8000_llm_tool',
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
    'llava-ft-4000_llm_tool': dict(
        abbr='llava-ft-4000_llm_tool',
        type=LagentAgent,
        agent_type=ReAct,
        max_turn=6,
        llm=dict(
            type=OpenAI,
            path='llava-ft-4000',
            key='EMPTY', # put your key here
            openai_api_base='http://222.29.51.128:12586/v1/chat/completions',
            query_per_second=1,
            max_seq_len=3072,
            stop='<|eot_id|>',
        ),
        tool_server='http://222.29.51.126:16181', # end-to-end
        # tool_meta='data/gta_dataset/toolmeta.json',
        batch_size=8,
    ),
    'llava-ft-nocaption_llm_tool': dict(
        abbr='llava-ft-nocaption_llm_tool',
        type=LagentAgent,
        agent_type=ReAct,
        max_turn=6,
        llm=dict(
            type=OpenAI,
            path='llava-ft-nocaption',
            key='EMPTY', # put your key here
            openai_api_base='http://222.29.51.128:12586/v1/chat/completions',
            query_per_second=1,
            max_seq_len=3072,
            stop='<|eot_id|>',
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
