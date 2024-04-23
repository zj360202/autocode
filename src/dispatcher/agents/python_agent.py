"""
python agent中比较难的地方在于，生成的很多的函数，在函数直接调用，怎么让模型可以很好的提示
可能需要每一个文件函数的列表和说明，方便在生成计划的时候，更加有条理
"""
import os
from dispatcher.agents.agent import format_agent_result
from dispatcher.agents.shell_agent import windows_shell_agent, linux_shell_agent


@format_agent_result
def run_python(code: str, 
               env_name: str = None,
               pip_info: str = None, 
               args_dict: dict = None, 
               return_keys: list = None):
    """
    执行python code，并返回结果

    Args:
        code (str): 代码主体部分
        env_name (str, optional): conda env环境，在用户提供需求的时候指定，默认是None
        pip_info (str, optional): pip需要安装的内容. Defaults to None.
        args_dict (dict, optional): python代码执行中需要传入的参数对{key:value}的形式
        return_keys (list, optional): 执行后，需要返回的字段列表
    Returns:
        dict: 需要返回的字典数据
    """
    if pip_info is not None:
        if os.system() == 'Windows':
            pips = pip_info.replace('\n', ';')
            windows_shell_agent(pips, env_name=env_name)
        else:
            pips = pip_info.replace('\n', ' && ')
            linux_shell_agent(pips, env_name=env_name)
    exec(code, args_dict)
    result = {}
    if return_keys and len(return_keys) > 0:
        for k in return_keys:
            result[k] = args_dict[k]
    return result


@format_agent_result
def merge_code(code: str, merge_file_path: str):
    """
    将传入python代码进行合并
    
    先判断import_info中的import或from信息是否已经包含在目标文件中
    如果不包含，才添加相关信息，如果包含就不添加了
    然后code直接追加到最后面
    Args:
        code (str): 代码主体部分
        merge_file_path (str): 需要合并的python代码路径
    """
    lines = []
    codes = []
    # 先获取原文件中的内容
    f = open(merge_file_path, 'r')
    for line in f.readlines():
        if not line.startswith('import') or not line.startswith('from'):
            codes.append(line)
        else:
            lines.append(line)
    
    # 将code中的import内容和代码正文进行分开
    new_code = ""
    imports = []
    cs = code.split('\n')
    for c in cs:
        if c.startswith('import') or c.startswith('from'):
            imports.append(c)
        else:
            new_code += c + '\n'
    
    # 判定新的import和from信息是否在原来的文件中存在
    if len(imports) != 0:
        for imp in imports:
            has_exists = False
            for line in lines:
                if line == imp:
                    has_exists = True
                    break
            if not has_exists:
                lines.append(imp)
    
    # 将所有数据写入文件，先写import或from信息，然后写入code部分
    with open(merge_file_path, 'w') as merge_file:
        for line in lines:
            merge_file.write(f'{line}\n')
        for c in codes:
            merge_file.write(f'{c}\n')
        merge_file.write(f'{code}\n')


@format_agent_result
def create_dir(dir_path: str):
    """
    创建目录
    Args:
        dir_path (str): 目录信息
    """
    if not os.path.exists:
        os.makedirs(dir_path, exist_ok=True)


@format_agent_result
def write_file(file_path: str, file_content: str):
    """
    写文件
    Args:
        file_path (str): 目标文件
        file_content (str): 文件内容
    """
    dir_path = os.path.dirname(file_path)
    create_dir(dir_path)

    with open(file_path, 'w') as merge_file:
        merge_file.write(file_content)


@format_agent_result
def append_file(file_path: str, file_content: str):
    """
    追加内容到文件中
    Args:
        file_path (str): 文件路径
        file_content (str): 文件内容
    """
    dir_path = os.path.dirname(file_path)
    create_dir(dir_path)

    with open(file_path, 'a') as merge_file:
        merge_file.write(file_content)
