"""
python agent中比较难的地方在于，生成的很多的函数，在函数直接调用，怎么让模型可以很好的提示
可能需要每一个文件函数的列表和说明，方便在生成计划的时候，更加有条理
"""
import os


def run_python(code: str, 
               pip_info: str = None, 
               import_info: str = None,
               args_dict: dict = None, 
               return_keys: list = None):
    """
    执行python code，并返回结果

    Args:
        code (str): 代码主体部分
        pip_info (str, optional): pip需要安装的内容. Defaults to None.
        import_info (str, optional): import或者from需要依赖的模块信息. Defaults to None.
        args_dict (dict, optional): python代码执行中需要传入的参数对{key:value}的形式
        return_keys (list, optional): 执行后，需要返回的字段列表
    Returns:
        dict: 需要返回的字典数据
    """
    if pip_info is not None:
        pips = pip_info.split('\n')
        for p in pips:
            
    exec(code, args_dict)
    result = {}
    if return_keys and len(return_keys) > 0:
        for k in return_keys:
            result[k] = args_dict[k]
    return result


def merge_code(code: str, merge_file_path: str, 
               import_info: str = None):
    """
    将传入python代码进行合并
    Args:
        code (str): 代码主体部分
        merge_file_path (str): 需要合并的python代码路径
        import_info (str, optional): import或者from需要依赖的模块信息
    """
    lines = []
    codes = []
    if import_info is not None:
        imports = import_info.split("\n")
        f = open(merge_file_path, 'r')
        for line in f.readlines():
            if not line.startswith('import') or not line.startswith('from'):
                continue
            lines.append(line)
        for imp in imports:
            has_exists = False
            for line in lines:
                if line == imp:
                    has_exists = True
                    break
            if not has_exists:
                lines.append(imp)
    with open(merge_file_path, 'w') as merge_file:
        merge_file.write(code)


def create_dir(dir_path: str):
    """
    创建目录
    Args:
        dir_path (str): 目录信息
    """
    if not os.path.exists:
        os.makedirs(dir_path, exist_ok=True)


def write_file(file_path: str, file_content: str):

    dir_path = os.path.dirname(file_path)
    create_dir(dir_path)

    with open(file_path, 'w') as merge_file:
        merge_file.write(file_content)


def append_file(file_path: str, file_content: str):
    dir_path = os.path.dirname(file_path)
    create_dir(dir_path)

    with open(file_path, 'a') as merge_file:
        merge_file.write(file_content)
