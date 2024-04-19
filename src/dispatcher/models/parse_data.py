

def _demand_pc(demand):
    """
    需要解析的内容: 项目目录
    """
    pass
    
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
def _answer_pc(answer: str):
    """
    模型回答的内容，需要其中抽取的内容如下:
    1. 项目结构
    2. 项目执行计划plans
    3. 项目验证计划check_plans

    Args:
        answer (str): 模型返回的内容
    """
    return {}


def parse_answer(demand_type: str, answer: str):
    """
    解析用户需求
    主要解析出：
    1. 用户需要管理项目的路径
    2. 用户对于项目的需求
    3. 用户希望使用的
    """
    if demand_type == 'pc':
        # 创建项目
        return _answer_pc(answer)
    
    