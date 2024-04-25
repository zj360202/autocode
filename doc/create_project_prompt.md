
用户需求: 
生成一个测试项目test, 只包含一个文件test.py, 包含一个打印hello word的方法

验证项目效果描述:
执行项目，输出hello world

描述规范是:
agent_name: agent_desc
    arg1(arg_type): arg1_desc
    arg2(arg_type): arg2_desc
agent列表如下，
merge_code: 将传入python代码进行合并.先判断import_info中的import或from信息是否已经包含在目标文件中.如果不包含，才添加相关信息，如果包含就不添加了.然后code直接追加到最后面.
	code (str): 代码主体部分
	merge_file_path (str): 需要合并的python代码路径
create_dir: 创建目录.
	dir_path (str): 目录信息
write_file: 写文件.
	file_path (str): 目标文件
	file_content (str): 文件内容
append_file: 追加内容到文件中.
	file_path (str): 文件路径
	file_content (str): 文件内容
shell_agent: windows 下执行command命令.
	command (str): windows shell command
	env_name (str, optional): conda环境，需要在用户提需求的时候进行指定


请给出对于用户需求和验证效果描述的执行计划，给出的计划必须满足如下要求：
1. 对自己的能力与行为的匹配进行review
2. 大局观与自我反思
3. 长期记忆对决策动作进行优化
4. 尽可能高效率的使用较少的动作来完成任务
5. 对于同一个任务，可以通过多种agent完成，如何让算法能够选择最好的解决方法
    比如：获取当期日期，可以通过python，web搜索，shell等，选择哪种最合适

项目结构 请用tree的方式描述项目的目录结果, <>的内容表示需要生成的内容：
<project_structure_tree>

任务拆解如下，<>的内容是需要进行替换的内容,如果arg_value是python代码用"""包含起来,对于可选参数，如果arg_value为None，则不用设定
用户需求:
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
验证项目效果描述(包含跳转项目目录和执行shell):
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