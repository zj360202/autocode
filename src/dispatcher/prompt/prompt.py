"""
https://zhuanlan.zhihu.com/p/622947810
主要目标：
1. 对自己的能力与行为的匹配进行review
2. 大局观与自我反思
3. 长期记忆对决策动作进行优化
4. 尽可能高效率的使用较少的动作来完成任务
5. 对于同一个任务，可以通过多种agent完成，如何让算法能够选择最好的解决方法
    比如：获取当期日期，可以通过python，web搜索，shell等，选择哪种最合适


设计流程如下：
1. 将每一个goals进行拆解，得到拆解的plan
2. 在拆解的过程中，要求算法对每一个plan给出所有agent的处理方式，如果无法处理则无需返回，并给出最优agent和理由
3. 在第一次执行的过程中，都以最有agent进行执行
4. 执行完成后，判定结果是否满足目标要求，如果满足则停止，如果不满足，则优化每一个plan，使用非最有的agent进行处理
"""


###################################################################################
# agent列表
prompt_agents = {
    'extract': [],
    'prompt':"""
描述规范是:
agent_name: agent_desc
    arg1(arg_type): arg1_desc
    arg2(arg_type): arg2_desc
agent列表如下，
{agent_infos}

请给出对于用户需求和验证效果描述的执行计划，给出的计划必须满足如下要求：
1. 对自己的能力与行为的匹配进行review
2. 大局观与自我反思
3. 长期记忆对决策动作进行优化
4. 尽可能高效率的使用较少的动作来完成任务
5. 对于同一个任务，可以通过多种agent完成，如何让算法能够选择最好的解决方法
    比如：获取当期日期，可以通过python，web搜索，shell等，选择哪种最合适
"""
}

###################################################################################
# 用户需求
prompt_user_demand_create_project_input = {
    'extract': [],
    'prompt':"""
用户需求: 
{demand}

验证项目效果描述:
{check_desc}
"""
}

prompt_user_demand_create_project_output = {
    'extract': ['用户需求', '验证项目'],
    'prompt':"""
项目结构 请用tree的方式描述项目的目录结果, <>的内容表示需要生成的内容：
<project_structure_tree>

任务拆解要求如下:
1. <>的内容是需要进行替换的内容
2. 如果arg_value是python代码用\"""包含起来
3. 对于可选参数，如果arg_value为None，则不用设定
4. 返回的必须是列表，如果有多个任务，在列表中添加新的任务json
5. 下面任务说明格式化是"任务+序号, 任务标题"，任务说明必须完整出现在回复中，不作变更

任务1, 用户需求任务拆解:
```json
[
    # 一个字典代表一个步骤
    {
        "desc": "<reasoning>",
        "agent": {
            "name": <agent_name>
            "args": {
                <arg_name>: <arg_value>
            }
        }
    }
]
```
任务2, 验证项目效果任务拆解(包含跳转项目目录和执行shell):
```json
[
    # 一个字典代表一个步骤
    {
        "desc": "<reasoning>",
        "agent": {
            "name": <agent_name>
            "args": {
                <arg_name>: <arg_value>
            }
        }
    }
]
```
"""
}

# 需求分析
prompt_demand_analyse_input = {
    'extract': [],
    'prompt':"""
使用python, 完成需求: {demand}
"""
}

###################################################################################
# python代码生成
# demand需求：来自用户或是通过模型生成的计划描述
prompt_python_code_input = {
    'extract': [],
    'prompt':"""
使用python, 完成需求: {demand}
"""
}

prompt_python_code_output = {
    'extract': ['pip安装内容', 'import相关内容', 'python代码'],
    'prompt':"""
python 代码生成，返回格式化如下，下面{content}中是需要生成和替换的内容
pip安装内容如下:
```shell
{content}
```

import相关内容如下:
```python
{content}
```

python代码内容如下:
```python
{content}
```
"""
}

###################################################################################
# 执行错误后，让模型修正
prompt_error_fix_input = {
    'extract': [],
    'prompt':"""
需求描述: 
{desc}

执行内容, agent信息:
{agent}

执行错误如下:
```shell
{err_msg}
```
"""
}

prompt_error_fix_output = {
    'extract': ['修正后的内容'],
    'prompt':"""
请修正错误，并给出修正后的内容
补充说明，agent信息的格式化：
{
    "desc": "<reasoning>",
    "agent": {
        "name": <agent_name>
        "args": {
            <arg_name>: <arg_value>
        }
    }
}
修复内容的格式化和上面一样，并且和agent信息保持一致，只修改arg_value的内容，其余内容不变
"""
}
