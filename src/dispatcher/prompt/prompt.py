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
from dispatcher.agents.agent import AgentFactory

###################################################################################
# 用户需求
agent_infos = ""
agent_func_mapping = AgentFactory.agent_mapping()
for k, v in agent_func_mapping.items():
    agent_infos += f'{v["desc"]}'

prompt_agents = f"""
描述规范是:
agent_name: agent_desc
    arg1(arg_type): arg1_desc
    arg2(arg_type): arg2_desc
agent列表如下，
{agent_infos}
"""

###################################################################################
# 用户需求
prompt_user_demand_create_project_input = """
用户需求: 
{demand}

验证项目效果描述:
{check_desc}

{prompt_agents}

请给出对于用户需求和验证效果描述的执行计划，给出的计划必须满足如下要求：
1. 对自己的能力与行为的匹配进行review
2. 大局观与自我反思
3. 长期记忆对决策动作进行优化
4. 尽可能高效率的使用较少的动作来完成任务
5. 对于同一个任务，可以通过多种agent完成，如何让算法能够选择最好的解决方法
    比如：获取当期日期，可以通过python，web搜索，shell等，选择哪种最合适
"""

prompt_user_demand_create_project_output = """
项目结构 请用tree的方式描述项目的目录结果, <>的内容表示需要生成的内容：
<project_structure_tree>

任务拆解如下，<>的内容是需要进行替换的内容
用户需求:
```json
[
    {
        "desc": "<reasoning>",
        "<agent_name>": {
            args: {
                <arg_name>: <arg_value>
            }
        }
    }
]
```
验证项目效果描述:
```json
[
    {
        "desc": "<reasoning>",
        "<agent_name>": {
            args: {
                <arg_name>: <arg_value>
            }
        }
    }
]
```
"""

# 需求分析
prompt_demand_analyse_input = """
使用python, 完成需求: {demand}
"""

prompt_demand_output = """
完成
"""

###################################################################################
# python代码生成
# demand需求：来自用户或是通过模型生成的计划描述
prompt_python_code_input = """
使用python, 完成需求: {demand}
"""

prompt_python_code_output = """
python 代码生成，返回格式化如下，下面{content}中是需要生成和替换的内容
pip 安装内容如下:
```shell
{content}
```

import或from相关内容如下:
```python
{content}
```

python代码内容如下:
```python
{content}
```
"""

###################################################################################

