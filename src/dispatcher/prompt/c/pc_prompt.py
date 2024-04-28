"""
创建项目中，e(效果优先)模式下的prompt
"""

###################################################################################
# 用户需求

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
6. 如果agent存在返回参数，且在后续流程中需要使用，可以在agent的output中，定义一个变量名称，放到param_name上, 
    以便在后续agent中的arg_value，使用${param_name}的方式进行引用

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
            },
            output: <param_name>
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
            },
            output: <param_name>
        }
    }
]
```
"""
}

###################################################################################
# 执行错误后，让模型修正
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
        },
        output: <param_name>
    }
}
修复内容的格式化和上面一样，并且和agent信息保持一致，只修改arg_value的内容，其余内容不变
"""
}
