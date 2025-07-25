import argparse
import os
import os.path as osp
import random
import sys
import time
from typing import Any

from mmengine.config import Config, ConfigDict
from mmengine.utils import mkdir_or_exist

from opencompass.registry import (ICL_INFERENCERS, ICL_PROMPT_TEMPLATES,
                                  ICL_RETRIEVERS, TASKS)
from opencompass.tasks.base import BaseTask
from opencompass.utils import (build_dataset_from_cfg, build_model_from_cfg,
                               get_infer_output_path, get_logger,
                               task_abbr_from_cfg)


@TASKS.register_module(force=(__name__ == '__main__'))  # A hack for script run
class OpenICLInferTask(BaseTask):
    """OpenICL Inference Task.

    This task is used to run the inference process.
    """

    name_prefix = 'OpenICLInfer'
    log_subdir = 'logs/infer'
    output_subdir = 'predictions'

    def __init__(self, cfg: ConfigDict):
        super().__init__(cfg)
        run_cfg = self.model_cfgs[0].get('run_cfg', {})
        self.num_gpus = run_cfg.get('num_gpus', 0)
        self.num_procs = run_cfg.get('num_procs', 1)
        self.logger = get_logger()

    def get_command(self, cfg_path, template):
        """Get the command template for the task.

        Args:
            cfg_path (str): The path to the config file of the task.
            template (str): The template which have '{task_cmd}' to format
                the command.
        """
        sys.path.append(os.getcwd())
        script_path = __file__
        backend_keys = ['VLLM', 'Lmdeploy']
        use_backend = any(
            key in str(self.model_cfgs[0].get('type', ''))
            or key in str(self.model_cfgs[0].get('llm', {}).get('type', ''))
            for key in backend_keys)
        if self.num_gpus > 0 and not use_backend:
            port = random.randint(12000, 32000)
            command = (f'torchrun --master_port={port} '
                       f'--nproc_per_node {self.num_procs} '
                       f'{script_path} {cfg_path}')
        else:
            python = sys.executable
            command = f'{python} {script_path} {cfg_path}'

        return template.format(task_cmd=command)

    def run(self, cur_model=None):
        self.logger.info(f'Task {task_abbr_from_cfg(self.cfg)}')
        for model_cfg, dataset_cfgs in zip(self.model_cfgs, self.dataset_cfgs):
            self.max_out_len = model_cfg.get('max_out_len', None)
            self.batch_size = model_cfg.get('batch_size', None)
            self.min_out_len = model_cfg.get('min_out_len', None)
            if cur_model:
                self.model = cur_model
            else:
                self.model = build_model_from_cfg(model_cfg) # self.model: <opencompass.models.lagent.LagentAgent object at 0x7701e95b1240>
                cur_model = self.model

            for dataset_cfg in dataset_cfgs:
                self.model_cfg = model_cfg # model_cfg:  {'abbr': 'qwen1.5-7b-chat', 'agent_type': 'lagent.agents.ReAct', 'batch_size': 8, 'llm': {'key': 'EMPTY', 'max_seq_len': 4096, 'openai_api_base': 'http://222.29.51.128:12580/v1/chat/completions', 'path': 'qwen1.5-7b-chat', 'query_per_second': 1, 'stop': '<|im_end|>', 'type': 'opencompass.models.OpenAI'}, 'max_turn': 10, 'tool_server': 'http://222.29.51.126:16181', 'type': 'opencompass.models.lagent.LagentAgent'}
                self.dataset_cfg = dataset_cfg # dataset_cfg:  {'abbr': 'gta_bench_0', 'eval_cfg': {'evaluator': {'mode': 'every', 'type': 'opencompass.datasets.gta_bench.GTABenchEvaluator'}}, 'infer_cfg': {'inferencer': {'infer_mode': 'every', 'type': 'opencompass.openicl.icl_inferencer.AgentInferencer'}, 'prompt_template': {'template': '{questions}', 'type': 'opencompass.openicl.icl_prompt_template.PromptTemplate'}, 'retriever': {'type': 'opencompass.openicl.icl_retriever.ZeroRetriever'}}, 'path': 'data/gta_dataset', 'reader_cfg': {'input_columns': ['dialogs', 'resources'], 'output_column': 'gt_answer', 'test_split': 'test', 'train_split': 'test', 'test_range': '[0:46]'}, 'type': 'opencompass.datasets.gta_bench.GTABenchDataset'}
                self.infer_cfg = self.dataset_cfg['infer_cfg'] # infer_cfg:  {'inferencer': {'infer_mode': 'every', 'type': 'opencompass.openicl.icl_inferencer.AgentInferencer'}, 'prompt_template': {'template': '{questions}', 'type': 'opencompass.openicl.icl_prompt_template.PromptTemplate'}, 'retriever': {'type': 'opencompass.openicl.icl_retriever.ZeroRetriever'}}
                self.dataset = build_dataset_from_cfg(self.dataset_cfg) # self.dataset: <opencompass.datasets.gta_bench.GTABenchDataset object at 0x78f3f7f34040>
                self.sub_cfg = {
                    'models': [self.model_cfg],
                    'datasets': [[self.dataset_cfg]],
                }
                out_path = get_infer_output_path(
                    self.model_cfg, self.dataset_cfg,
                    osp.join(self.work_dir, 'predictions'))
                if osp.exists(out_path):
                    continue
                self._inference()

    def _inference(self):
        self.logger.info(
            f'Start inferencing {task_abbr_from_cfg(self.sub_cfg)}')

        assert hasattr(self.infer_cfg, 'ice_template') or hasattr(self.infer_cfg, 'prompt_template'), \
            'Both ice_template and prompt_template cannot be None simultaneously.'  # noqa: E501
        if hasattr(self.infer_cfg, 'ice_template'):
            ice_template = ICL_PROMPT_TEMPLATES.build(
                self.infer_cfg['ice_template'])

        if hasattr(self.infer_cfg, 'prompt_template'):
            prompt_template = ICL_PROMPT_TEMPLATES.build(
                self.infer_cfg['prompt_template'])
            """
            prompt_template: 
            PromptTemplate({
                template: {questions},
                ice_token: None
            })
            """

        retriever_cfg = self.infer_cfg['retriever'].copy()
        retriever_cfg['dataset'] = self.dataset
        retriever = ICL_RETRIEVERS.build(retriever_cfg) # retriever: <opencompass.openicl.icl_retriever.icl_zero_retriever.ZeroRetriever object at 0x7d7c475b2f80>

        # set inferencer's default value according to model's config'
        inferencer_cfg = self.infer_cfg['inferencer']
        inferencer_cfg['model'] = self.model
        self._set_default_value(inferencer_cfg, 'max_out_len',
                                self.max_out_len)
        self._set_default_value(inferencer_cfg, 'min_out_len',
                                self.min_out_len)
        self._set_default_value(inferencer_cfg, 'batch_size', self.batch_size)
        inferencer_cfg['max_seq_len'] = self.model_cfg.get('max_seq_len')
        inferencer = ICL_INFERENCERS.build(inferencer_cfg) # inferencer: <opencompass.openicl.icl_inferencer.icl_agent_inferencer.AgentInferencer object at 0x76c72c09efe0>

        out_path = get_infer_output_path(
            self.model_cfg, self.dataset_cfg,
            osp.join(self.work_dir, 'predictions'))
        out_dir, out_file = osp.split(out_path)
        mkdir_or_exist(out_dir)

        if hasattr(self.infer_cfg, 'prompt_template') and \
                hasattr(self.infer_cfg, 'ice_template'):
            inferencer.inference(retriever,
                                 ice_template=ice_template,
                                 prompt_template=prompt_template,
                                 output_json_filepath=out_dir,
                                 output_json_filename=out_file)
        elif hasattr(self.infer_cfg, 'prompt_template'):
            inferencer.inference(retriever,
                                 prompt_template=prompt_template,
                                 output_json_filepath=out_dir,
                                 output_json_filename=out_file)
        else:
            inferencer.inference(retriever,
                                 ice_template=ice_template,
                                 output_json_filepath=out_dir,
                                 output_json_filename=out_file)

    def _set_default_value(self, cfg: ConfigDict, key: str, value: Any):
        if key not in cfg:
            cfg[key] = value


def parse_args():
    parser = argparse.ArgumentParser(description='Model Inferencer')
    parser.add_argument('config', help='Config file path')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()
    cfg = Config.fromfile(args.config)
    start_time = time.time()
    inferencer = OpenICLInferTask(cfg)
    inferencer.run()
    end_time = time.time()
    get_logger().info(f'time elapsed: {end_time - start_time:.2f}s')
