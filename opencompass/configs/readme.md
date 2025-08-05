# eval_config 格式解释

```python
# 每个模型的config是一个字典，字典的key是你要在测试里填的那个--eval_mode
'chatgpt-4o-latest_vlm': dict(
    abbr='chatgpt-4o-latest_vlm', # 没啥用的内部文件名字，一般设置成和key一样就行
    type=LagentAgentVisual, # choices: [LagentAgent(LLM-agent，不传递图), LagentAgentVisual(VLM-agent，传递图), LagentAgentVisualLocal(已废弃，见到就全换成Visual就行)
    agent_type=ReAct, # agent_type，一般不动
    max_turn=1, # react最多对话轮数，在w/o tool的时候=1，其他时候一般=10（如果=10太慢可以酌情下调）
    llm=dict(
        type=OpenAIVisualDummy, # choices: [OpenAI(LLM-w/tool), OpenAIVisual(VLM-w/tool), OpenAIVisualDummy(VLM-w/o tool，实现方式是手动截取qa-pair丢弃其他所有对话)]
        path='chatgpt-4o-latest', # 模型的名字，如果是api-based这里填model_name.png里面的名字，如果是本地部署的则填lmdeploy运行时的那个--model-name
        key='sk-NJXrSjHdKph9kk1K9a81A68fA1Be4e7798EbB622Fa5cA062', # api key，本地部署可以不填
        openai_api_base='https://29qg.com/v1', # api base，本地部署要改成lmdeploy的那个port
        query_per_second=1, # 貌似没啥用
        max_seq_len=4096, # 模型输出的length，貌似没啥用
        retry=10 # retry次数，貌似没啥用（一般不会卡住）
    ),
    tool_server='http://222.29.51.126:16181', # 填agentlego的port，如果是step-by-step可以去掉这一行（step-by-step不实际调用工具）
    tool_meta='data/gta_dataset/toolmeta.json', # 填toolmeta的路径（工具信息），如果是end-to-end可以去掉这一行
    batch_size=8,
),

```