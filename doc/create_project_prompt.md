用户需求:
生成一个测试项目test, 只包含一个文件test.py, 包含一个打印hello word的方法

验证项目效果描述:
执行项目文件，输出hello world


描述规范是:
agent_name: agent_desc
    arg1(arg_type): arg1_desc
    arg2(arg_type): arg2_desc
agent列表如下，
run_python: 执行python code，并返回结果.
        code (str): 代码主体部分，代码不能为None或空
        pip_info (str, optional): pip需要安装的内容. Defaults to None.
        import_info (str, optional): import或者from需要依赖的模块信息. Defaults to None.
        args_dict (dict, optional): python代码执行中需要传入的参数对{key:value}的形式
        return_keys (list, optional): 执行后，需要返回的字段列表
merge_code: 将传入python代码进行合并.
        code (str): 代码主体部分，代码不能为None或空
        merge_file_path (str): 需要合并的python代码路径
        pip_info (str, optional): pip需要安装的内容
        import_info (str, optional): import或者from需要依赖的模块信息
create_dir: 创建目录.
        dir_path (str): 目录信息
        file_path (str): 目标文件
        file_content (str): 文件内容
write_file: 写文件.
        file_path (str): 目标文件
        file_content (str): 文件内容
windows_shell_agent: windows 下执行command命令
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

任务拆解说明如下，标题必须在回复出现，<>的内容是需要进行替换的内容,python代码用"""包含
用户需求拆解如下:
```json
[
    # 一个字典代表一个步骤
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
验证项目效果拆解如下:
```json
[
    # 一个字典代表一个步骤
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
