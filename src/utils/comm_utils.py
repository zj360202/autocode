import os
import re
import inspect

from utils.constants import AGENT_TEMP_DOC, PATTERN_PARAMS


def get_full_path(relation_path, project_path):
    """
    判定相对路径是否是相对路径，如果是，则使用项目路径补全路径
    """
    if relation_path.startswith('.'):
        relation_path = os.path.join(project_path, str(relation_path[2:]))
    elif '/' not in relation_path:
        relation_path = os.path.join(project_path, relation_path)
    return relation_path


def agent_desc(agent_name, func):
    """
    主要是agent的内容，需要详细提供给大模型，以便大模型可以更好的通过这些agent完成任务计划
    功能如下：
    1. 校验doc格式化是否正确，参照constants.AGENT_TEMP_DOC样式
    2. 提取函数描述内容和参数描述内容
    3. 

    Args:
        agent_name (_type_): agent名称，是
        func (_type_): 函数

    Raises:
        ValueError: _description_
        ValueError: _description_
        ValueError: _description_
    """
    # 获取函数的doc注释
    func_doc = inspect.getdoc(func)
    # 获取参数信息
    func_args = inspect.getfullargspec(func.__wrapped__)
    # 提取参数列表
    arg_list = func_args.args
    ################################################################
    # 解析doc
    doc_lines = func_doc.split('\n')
    # 解析函数desc
    func_desc = ''
    for line in doc_lines:
        if line.strip() == '':
            continue
        if line.strip() == 'Args:':
            break
        func_desc += f'{line}.'

    # 解析参数desc
    func_args_desc, start = [], False
    match_arg = []
    for line in doc_lines:
        line = line.strip()
        if line == 'Args:':
            start = True
        elif 'Return' in line:
            break
        elif start:
            arg_left = line.split(':')[0]
            if '(' not in arg_left or ')' not in arg_left:
                raise ValueError(f'agent: {agent_name} 的{arg_left}格式不正确，doc注释标准模板如下\n{AGENT_TEMP_DOC}')
            arg_name = arg_left.split('(')[0].strip()
            if arg_name not in arg_list:
                raise ValueError(f'agent: {agent_name} 的doc注释描述中的参数:{arg_name}和实际参数未匹配')
            func_args_desc.append(line)
            for i, arg in enumerate(arg_list):
                if arg == arg_name:
                    match_arg.append(i)
    if len(match_arg) != len(arg_list):
        raise ValueError(f'agent: {agent_name} 的doc注释中未将所有的参数进行描述完全')
    return func_desc, func_args_desc

def find_params(text):
    """
    可以从文本中找到${}中的内容
    Args:
        text (_type_): 包含变量的文本
    Returns:
        list: 变量名称列表
    """
    pattern = re.compile(PATTERN_PARAMS)

    return pattern.findall(text)
