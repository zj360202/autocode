import json


def _parse_md(markdown: str, titles: list):
    """
    解析markdown中的内容
    Args:
        markdown (str): markdown内容
        titles (list): 需要抽取的内容标题
    """
    if titles is None or len(titles) == 0:
        return {}
    title_idx = 0
    contents = {}
    content, find_title, start_content = "", -1, False
    # 获取```类型，方便后续进行转化，目前主要是json需要转化，其他占不需要
    content_type = 'shell'

    # 判定当前内容是否在三个引号中，表示是python code
    tri_quota = False
    for line in markdown.split('\n'):
        if title_idx < len(titles) and titles[title_idx] in line:
            if find_title != -1:
                if content_type == 'json':
                    contents[titles[title_idx-1]] = json.loads(content)
                else:
                    contents[titles[title_idx-1]] = content
                content = ""
            find_title = title_idx
            title_idx = title_idx + 1
        elif find_title >= 0 and '```' in line:
            # 判定是否在输出中，prompt要求，输出需要执行的内容必须在```中，而且需要尽量保证每一个```中的内容是原子性的
            # 比如: 一个```json 中尽量不要存在两个json,后续会进行优化判定，当代码是不支持的
            new_line = line.replace('\n', '').strip()
            if len(new_line) > 3:
                content_type = str(new_line[3:])
            start_content = not start_content
        elif start_content:
            # python代码中的"""转义json会报错
            # python代码中的换行也会报错，都需要转义
            if '"""' in line:
                line = line.replace('"""', '"')
                tri_quota = not tri_quota
            if tri_quota:
                line = line.replace('\n', '@@')
            content += line
    if content != '':
        # 最后一个需要放到字典中去
        if content_type == 'json':
            contents[titles[title_idx-1]] = json.loads(content)
        else:
            contents[titles[title_idx-1]] = content
    return contents

def _demand_pc(demand: str, titles: list):
    """
    需要解析的内容: 项目目录
    """
    return {}
    
def parse_demand(demand_type: str, demand: str):
    """
    解析在用户需求中的关键信息
    Args:
        demand_type (str): 需求类型
        demand (str): 需求描述
    """
    if demand_type == 'pc':
        # 创建项目
        _demand_pc(demand)

##############################################################
# Answer
def _answer_pc(answer: str, titles: list):
    """
    模型回答的内容，需要其中抽取的内容如下:
    1. 项目结构
    2. 项目执行计划plans
    3. 项目验证计划check_plans

    Args:
        answer (str): 模型返回的内容
    """
    return _parse_md(answer, titles)

def _answer_error_fix(answer: str, titles: list):
    """
    模型回答的内容，需要其中抽取的内容如下:
    1. 单个执行计划(目前主要是python, shell错误的概率比较大)

    Args:
        answer (str): 模型返回的内容
    """
    return _parse_md(answer, titles)

def parse_answer(answer: str, titles: str):
    """
    解析用户需求
    主要解析出：
    1. 用户需要管理项目的路径
    2. 用户对于项目的需求
    3. 用户希望使用的
    """
    return _parse_md(answer, titles=titles)
    
    