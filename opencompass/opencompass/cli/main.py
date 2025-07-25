# flake8: noqa
# yapf: disable
import argparse
import getpass
import os
import os.path as osp
from datetime import datetime

from mmengine.config import Config, DictAction

from opencompass.registry import PARTITIONERS, RUNNERS, build_from_cfg
from opencompass.runners import SlurmRunner
from opencompass.summarizers import DefaultSummarizer
from opencompass.utils import LarkReporter, get_logger
from opencompass.utils.run import (fill_eval_cfg, fill_infer_cfg,
                                   get_config_from_arg)


def parse_args():
    parser = argparse.ArgumentParser(description='Run an evaluation task')
    parser.add_argument('config', nargs='?', help='Train config file path')

    # add mutually exclusive args `--slurm` `--dlc`, defaults to local runner
    # if "infer" or "eval" not specified
    launch_method = parser.add_mutually_exclusive_group()
    launch_method.add_argument('--slurm',
                               action='store_true',
                               default=False,
                               help='Whether to force tasks to run with srun. '
                               'If True, `--partition(-p)` must be set. '
                               'Defaults to False')
    launch_method.add_argument('--dlc',
                               action='store_true',
                               default=False,
                               help='Whether to force tasks to run on dlc. If '
                               'True, `--aliyun-cfg` must be set. Defaults'
                               ' to False')
    # Add shortcut parameters (models, datasets and summarizer)
    parser.add_argument('--models', nargs='+', help='', default=None)
    parser.add_argument('--datasets', nargs='+', help='', default=None)
    parser.add_argument('--summarizer', help='', default=None)
    # add general args
    parser.add_argument('--debug',
                        help='Debug mode, in which scheduler will run tasks '
                        'in the single process, and output will not be '
                        'redirected to files',
                        action='store_true',
                        default=False)
    parser.add_argument('--dry-run',
                        help='Dry run mode, in which the scheduler will not '
                        'actually run the tasks, but only print the commands '
                        'to run',
                        action='store_true',
                        default=False)
    parser.add_argument(
        '-a', '--accelerator',
        help='Infer accelerator, support vllm and lmdeploy now.',
        choices=['vllm', 'lmdeploy', None],
        default=None,
        type=str)
    parser.add_argument('-m',
                        '--mode',
                        help='Running mode. You can choose "infer" if you '
                        'only want the inference results, or "eval" if you '
                        'already have the results and want to evaluate them, '
                        'or "viz" if you want to visualize the results.',
                        choices=['all', 'infer', 'eval', 'viz'],
                        default='all',
                        type=str)
    parser.add_argument('-r',
                        '--reuse',
                        nargs='?',
                        type=str,
                        const='latest',
                        help='Reuse previous outputs & results, and run any '
                        'missing jobs presented in the config. If its '
                        'argument is not specified, the latest results in '
                        'the work_dir will be reused. The argument should '
                        'also be a specific timestamp, e.g. 20230516_144254')
    parser.add_argument('-w',
                        '--work-dir',
                        help='Work path, all the outputs will be '
                        'saved in this path, including the slurm logs, '
                        'the evaluation results, the summary results, etc.'
                        'If not specified, the work_dir will be set to '
                        'outputs/default.',
                        default=None,
                        type=str)
    parser.add_argument(
        '--config-dir',
        default='configs',
        help='Use the custom config directory instead of config/ to '
        'search the configs for datasets, models and summarizers',
        type=str)
    parser.add_argument('-l',
                        '--lark',
                        help='Report the running status to lark bot',
                        action='store_true',
                        default=False)
    parser.add_argument('--max-num-workers',
                        help='Max number of workers to run in parallel. '
                        'Will be overrideen by the "max_num_workers" argument '
                        'in the config.',
                        type=int,
                        default=1)
    parser.add_argument('--max-workers-per-gpu',
                        help='Max task to run in parallel on one GPU. '
                        'It will only be used in the local runner.',
                        type=int,
                        default=1)
    parser.add_argument(
        '--retry',
        help='Number of retries if the job failed when using slurm or dlc. '
        'Will be overrideen by the "retry" argument in the config.',
        type=int,
        default=2)
    parser.add_argument(
        '--dump-eval-details',
        help='Whether to dump the evaluation details, including the '
        'correctness of each sample, bpb, etc.',
        action='store_true',
    )
    # add eval mode
    parser.add_argument('--eval_mode',
                        help="The mode of evaluation, in format of 'model_vlm/llm_tool",
                        required=True)
    # set srun args
    slurm_parser = parser.add_argument_group('slurm_args')
    parse_slurm_args(slurm_parser)
    # set dlc args
    dlc_parser = parser.add_argument_group('dlc_args')
    parse_dlc_args(dlc_parser)
    # set hf args
    hf_parser = parser.add_argument_group('hf_args')
    parse_hf_args(hf_parser)
    # set custom dataset args
    custom_dataset_parser = parser.add_argument_group('custom_dataset_args')
    parse_custom_dataset_args(custom_dataset_parser)
    args = parser.parse_args()
    if args.slurm:
        assert args.partition is not None, (
            '--partition(-p) must be set if you want to use slurm')
    if args.dlc:
        assert os.path.exists(args.aliyun_cfg), (
            'When launching tasks using dlc, it needs to be configured '
            'in "~/.aliyun.cfg", or use "--aliyun-cfg $ALiYun-CFG_Path"'
            ' to specify a new path.')
    return args


def parse_slurm_args(slurm_parser):
    """These args are all for slurm launch."""
    slurm_parser.add_argument('-p',
                              '--partition',
                              help='Slurm partition name',
                              default=None,
                              type=str)
    slurm_parser.add_argument('-q',
                              '--quotatype',
                              help='Slurm quota type',
                              default=None,
                              type=str)
    slurm_parser.add_argument('--qos',
                              help='Slurm quality of service',
                              default=None,
                              type=str)


def parse_dlc_args(dlc_parser):
    """These args are all for dlc launch."""
    dlc_parser.add_argument('--aliyun-cfg',
                            help='The config path for aliyun config',
                            default='~/.aliyun.cfg',
                            type=str)




def parse_hf_args(hf_parser):
    """These args are all for the quick construction of HuggingFace models."""
    hf_parser.add_argument('--hf-type', type=str, choices=['base', 'chat'], default='chat', help='The type of the HuggingFace model, base or chat')
    hf_parser.add_argument('--hf-path', type=str, help='The path to the HuggingFace model, e.g. "facebook/opt-125m", required')
    hf_parser.add_argument('--model-kwargs', nargs='+', action=DictAction, default={}, help='The kwargs for the HuggingFace model')
    hf_parser.add_argument('--tokenizer-path', type=str, help='The path to the HuggingFace tokenizer, same as --hf-path if not specified')
    hf_parser.add_argument('--tokenizer-kwargs', nargs='+', action=DictAction, default={}, help='The kwargs for the tokenizer')
    hf_parser.add_argument('--peft-path', type=str, help='The path to the PEFT model')
    hf_parser.add_argument('--peft-kwargs', nargs='+', action=DictAction, default={}, help='The kwargs for the PEFT model')
    hf_parser.add_argument('--generation-kwargs', nargs='+', action=DictAction, default={}, help='The kwargs for the generation')
    hf_parser.add_argument('--max-seq-len', type=int, help='The max sequence length for the HuggingFace model')
    hf_parser.add_argument('--max-out-len', type=int, default=256, help='The max output length for the HuggingFace model')
    hf_parser.add_argument('--min-out-len', type=int, default=1, help='The min output length for the HuggingFace model')
    hf_parser.add_argument('--batch-size', type=int, default=8, help='The batch size for the HuggingFace model')
    hf_parser.add_argument('--num-gpus', type=int, default=None, help='Deprecated, please use --hf-num-gpus instead')
    hf_parser.add_argument('--hf-num-gpus', type=int, default=1, help='The number of GPUs for the HuggingFace model passed via cli')
    hf_parser.add_argument('--pad-token-id', type=int, help='The pad token id for the HuggingFace model')
    hf_parser.add_argument('--stop-words', nargs='+', default=[], help='The stop words for the HuggingFace model')


def parse_custom_dataset_args(custom_dataset_parser):
    """These args are all for the quick construction of custom datasets."""
    custom_dataset_parser.add_argument('--custom-dataset-path', type=str)
    custom_dataset_parser.add_argument('--custom-dataset-meta-path', type=str)
    custom_dataset_parser.add_argument('--custom-dataset-data-type',
                                       type=str,
                                       choices=['mcq', 'qa'])
    custom_dataset_parser.add_argument('--custom-dataset-infer-method',
                                       type=str,
                                       choices=['gen', 'ppl'])


def main():
    args = parse_args()

    if args.num_gpus is not None:
        raise ValueError('The `--num-gpus` argument is deprecated, please use '
                         '`--hf-num-gpus` to describe number of gpus used for '
                         'the HuggingFace model instead.')

    if args.dry_run:
        args.debug = True
    # Namespace(config='configs/eval_gta_bench.py', slurm=False, dlc=False, models=None, datasets=None, summarizer=None, debug=True, dry_run=False, accelerator=None, mode='all', reuse=None, work_dir=None, config_dir='configs', lark=False, max_num_workers=32, max_workers_per_gpu=1, retry=2, dump_eval_details=False, partition='llmit', quotatype='auto', qos=None, aliyun_cfg='~/.aliyun.cfg', hf_type='chat', hf_path=None, model_kwargs={}, tokenizer_path=None, tokenizer_kwargs={}, peft_path=None, peft_kwargs={}, generation_kwargs={}, max_seq_len=None, max_out_len=256, min_out_len=1, batch_size=8, num_gpus=None, hf_num_gpus=1, pad_token_id=None, stop_words=[], custom_dataset_path=None, custom_dataset_meta_path=None, custom_dataset_data_type=None, custom_dataset_infer_method=None)

    # initialize logger
    logger = get_logger(log_level='DEBUG' if args.debug else 'INFO')

    cfg = get_config_from_arg(args)
    # Config (path: configs/eval_gta_bench.py): {'datasets': [{'abbr': 'gta_bench', 'type': GTABenchDataset, 'path': 'data/gta_dataset', 'reader_cfg': {'input_columns': ['dialogs', 'resources'], 'output_column': 'gt_answer', 'train_split': 'test', 'test_split': 'test'}, 'infer_cfg': {'prompt_template': {'type': PromptTemplate, 'template': '{questions}'}, 'retriever': {'type': ZeroRetriever}, 'inferencer': {'type': AgentInferencer, 'infer_mode': 'every'}}, 'eval_cfg': {'evaluator': {'type': GTABenchEvaluator, 'mode': 'every'}}}], 'ReAct': ReAct, 'read_base': <function read_base at 0x7a8789597d00>, 'OpenAI': OpenAI, 'Qwen': Qwen, 'Gemini': Gemini, 'LagentAgent': LagentAgent, 'SizePartitioner': SizePartitioner, 'LocalRunner': LocalRunner, 'OpenICLInferTask': OpenICLInferTask, 'models': [{'abbr': 'qwen1.5-7b-chat', 'type': LagentAgent, 'agent_type': ReAct, 'max_turn': 10, 'llm': {'type': OpenAI, 'path': 'qwen1.5-7b-chat', 'key': 'EMPTY', 'openai_api_base': 'http://222.29.51.128:12580/v1/chat/completions', 'query_per_second': 1, 'max_seq_len': 4096, 'stop': '<|im_end|>'}, 'tool_server': 'http://222.29.51.128:16181', 'batch_size': 8}], 'infer': {'partitioner': {'type': SizePartitioner, 'max_task_size': 50, 'gen_task_coef': 1}, 'runner': {'type': LocalRunner, 'task': {'type': OpenICLInferTask}}}}
    if args.work_dir is not None:
        cfg['work_dir'] = args.work_dir
    else:
        cfg.setdefault('work_dir', os.path.join('outputs', 'default'))

    # cfg_time_str defaults to the current time
    cfg_time_str = dir_time_str = datetime.now().strftime('%Y%m%d_%H%M%S')
    if args.reuse:
        if args.reuse == 'latest':
            if not os.path.exists(cfg.work_dir) or not os.listdir(
                    cfg.work_dir):
                logger.warning('No previous results to reuse!')
            else:
                dirs = os.listdir(cfg.work_dir)
                dir_time_str = sorted(dirs)[-1]
        else:
            dir_time_str = args.reuse
        logger.info(f'Reusing experiements from {dir_time_str}')
    elif args.mode in ['eval', 'viz']:
        raise ValueError('You must specify -r or --reuse when running in eval '
                         'or viz mode!')

    # update "actual" work_dir
    cfg['work_dir'] = osp.join(cfg.work_dir, dir_time_str)
    os.makedirs(osp.join(cfg.work_dir, 'configs'), exist_ok=True)

    # dump config
    output_config_path = osp.join(cfg.work_dir, 'configs',
                                  f'{cfg_time_str}.py')
    cfg.dump(output_config_path)
    # Config is intentally reloaded here to avoid initialized
    # types cannot be serialized
    cfg = Config.fromfile(output_config_path, format_python_code=False)

    # report to lark bot if specify --lark
    if not args.lark:
        cfg['lark_bot_url'] = None
    elif cfg.get('lark_bot_url', None):
        content = f'{getpass.getuser()}\'s task has been launched!'
        LarkReporter(cfg['lark_bot_url']).post(content)

    if args.mode in ['all', 'infer']:
        # When user have specified --slurm or --dlc, or have not set
        # "infer" in config, we will provide a default configuration
        # for infer
        if (args.dlc or args.slurm) and cfg.get('infer', None):
            logger.warning('You have set "infer" in the config, but '
                           'also specified --slurm or --dlc. '
                           'The "infer" configuration will be overridden by '
                           'your runtime arguments.')

        if args.dlc or args.slurm or cfg.get('infer', None) is None:
            fill_infer_cfg(cfg, args)

        if args.partition is not None:
            if RUNNERS.get(cfg.infer.runner.type) == SlurmRunner:
                cfg.infer.runner.partition = args.partition
                cfg.infer.runner.quotatype = args.quotatype
        else:
            logger.warning('SlurmRunner is not used, so the partition '
                           'argument is ignored.')
        if args.debug:
            cfg.infer.runner.debug = True
        if args.lark:
            cfg.infer.runner.lark_bot_url = cfg['lark_bot_url']
        cfg.infer.partitioner['out_dir'] = osp.join(cfg['work_dir'],
                                                    'predictions/')
        partitioner = PARTITIONERS.build(cfg.infer.partitioner)
        tasks = partitioner(cfg)
        """
tasks:
[Config (path: None): 
    {
        'models': 
            [{
                'abbr': 'qwen1.5-7b-chat', 
                'agent_type': 'lagent.agents.ReAct', 
                'batch_size': 8, 
                'llm': 
                {
                    'key': 'EMPTY', 
                    'max_seq_len': 4096, 
                    'openai_api_base': 'http://222.29.51.128:12580/v1/chat/completions', 
                    'path': 'qwen1.5-7b-chat', 
                    'query_per_second': 1, 
                    'stop': '<|im_end|>', 
                    'type': 'opencompass.models.OpenAI'
                }, 
                'max_turn': 10, 
                'tool_server': 'http://222.29.51.128:16181', 
                'type': 'opencompass.models.lagent.LagentAgent'
            }], 
        'datasets': 
            [[{
                'abbr': 'gta_bench_0/1/2/3/4', 
                'eval_cfg': 
                {
                    'evaluator': 
                        {
                            'mode': 'every', 
                            'type': 'opencompass.datasets.gta_bench.GTABenchEvaluator'
                        }
                }, 
                'infer_cfg': 
                {
                    'inferencer': 
                    {
                        'infer_mode': 'every', 
                        'type': 'opencompass.openicl.icl_inferencer.AgentInferencer'
                    }, 
                    'prompt_template': 
                    {
                        'template': '{questions}', 
                        'type': 'opencompass.openicl.icl_prompt_template.PromptTemplate'
                    }, 
                    'retriever': 
                    {
                        'type': 'opencompass.openicl.icl_retriever.ZeroRetriever'
                    }
                }, 
                'path': 'data/gta_dataset', 
                'reader_cfg': 
                {
                    'input_columns': ['dialogs', 'resources'], 
                    'output_column': 'gt_answer', 
                    'test_split': 'test', 
                    'train_split': 'test', 
                    'test_range': '[0:46]/[46:92]/[92:138]/[138:184]/[184:230]'
                }, 
                'type': 'opencompass.datasets.gta_bench.GTABenchDataset'
            }]], 
        'work_dir': 'outputs/default/20241019_193558'
    }, 
        """
        if args.dry_run:
            return
        runner = RUNNERS.build(cfg.infer.runner)
        # Add extra attack config if exists
        if hasattr(cfg, 'attack'):
            for task in tasks:
                cfg.attack.dataset = task.datasets[0][0].abbr
                task.attack = cfg.attack
        runner(tasks)

    # evaluate
    if args.mode in ['all', 'eval']:
        # When user have specified --slurm or --dlc, or have not set
        # "eval" in config, we will provide a default configuration
        # for eval
        if (args.dlc or args.slurm) and cfg.get('eval', None):
            logger.warning('You have set "eval" in the config, but '
                           'also specified --slurm or --dlc. '
                           'The "eval" configuration will be overridden by '
                           'your runtime arguments.')

        if args.dlc or args.slurm or cfg.get('eval', None) is None:
            fill_eval_cfg(cfg, args)
        if args.dump_eval_details:
            cfg.eval.runner.task.dump_details = True

        if args.partition is not None:
            if RUNNERS.get(cfg.eval.runner.type) == SlurmRunner:
                cfg.eval.runner.partition = args.partition
                cfg.eval.runner.quotatype = args.quotatype
            else:
                logger.warning('SlurmRunner is not used, so the partition '
                               'argument is ignored.')
        if args.debug:
            cfg.eval.runner.debug = True
        if args.lark:
            cfg.eval.runner.lark_bot_url = cfg['lark_bot_url']
        cfg.eval.partitioner['out_dir'] = osp.join(cfg['work_dir'], 'results/')
        partitioner = PARTITIONERS.build(cfg.eval.partitioner)
        tasks = partitioner(cfg)
        if args.dry_run:
            return
        runner = RUNNERS.build(cfg.eval.runner)

        # For meta-review-judge in subjective evaluation
        if isinstance(tasks, list) and len(tasks) != 0 and isinstance(
                tasks[0], list):
            for task_part in tasks:
                runner(task_part)
        else:
            # tasks和上面相同但多了一个key: 'eval': {'runner': {'task': {}}}
            runner(tasks)

    # visualize
    if args.mode in ['all', 'eval', 'viz']:
        summarizer_cfg = cfg.get('summarizer', {})
        if not summarizer_cfg or summarizer_cfg.get('type', None) is None:
            summarizer_cfg['type'] = DefaultSummarizer
        summarizer_cfg['config'] = cfg
        summarizer = build_from_cfg(summarizer_cfg) # summarizer: <opencompass.summarizers.default.DefaultSummarizer object at 0x788425e87640>
        summarizer.summarize(time_str=cfg_time_str)



if __name__ == '__main__':
    main()
