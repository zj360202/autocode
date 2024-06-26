from loguru import logger

from .prompt import prompt_demand_to_plan, prompt_agents
from .prompt import prompt_user_demand_create_project_input, prompt_error_fix_input

from dispatcher.prompt.c.pc_prompt import prompt_user_demand_create_project_output as c_ud_pc, prompt_error_fix_output as c_ef
from dispatcher.prompt.e.pc_prompt import prompt_user_demand_create_project_output as e_ud_pc, prompt_error_fix_output as e_ef
from dispatcher.agents.agent import AgentFactory

agent_infos = ""

def _load_agent():
    """
    初始化agent信息
    """
    global agent_infos
    if agent_infos == "":
        agent_func_mapping = AgentFactory.agent_mapping()
        for k, v in agent_func_mapping.items():
            agent_infos += f'{v["desc"]}'
            
def prompt_demand_format(user_demand: str, search_info: str):
    """
    通过搜索完善用户需求，并将用户需求拆解完成计划
    """
    # 开始初始化prompt
    extracts = []
    prompt = ""
    
    # 配置用户需求信息
    extracts += prompt_demand_to_plan['extract']
    prompt = prompt_demand_to_plan['prompt'].format(demand=user_demand, search_info=search_info)
    
    return extracts, prompt
    

def prompt_pc(project_subject: str, check_desc: str, strategy: str='c'):
    # 初始化agent信息
    _load_agent()
    
    # 开始初始化prompt
    extracts = []
    prompt = ""
    
    # 配置用户需求信息
    extracts += prompt_user_demand_create_project_input['extract']
    temp_prompt = prompt_user_demand_create_project_input['prompt']
    prompt = temp_prompt.format(demand=project_subject, 
                                check_desc=check_desc)
    # 配置agent信息
    extracts += prompt_agents['extract']
    prompt += prompt_agents['prompt'].format(agent_infos=agent_infos)
    
    logger.debug(f'strategy:{strategy}')
    # 配置输出格式化
    if strategy == 'c':
        extracts += c_ud_pc['extract']
        prompt += c_ud_pc['prompt']
    else:
        extracts += e_ud_pc['extract']
        prompt += e_ud_pc['prompt']
    
    return extracts, prompt

def prompt_fix_error(demand_desc: str, agent_info: str, err_msg: str, strategy: str='c'):
    # 开始初始化prompt
    extracts = prompt_error_fix_input['extract']
    prompt = prompt_error_fix_input['prompt'].format(demand_desc=demand_desc, agent_info=agent_info, err_msg=err_msg)
    if strategy == 'c':
        extracts += c_ef['extract']
        prompt += c_ef['prompt']
    else:
        extracts += e_ef['extract']
        prompt += e_ef['prompt']
    
    return extracts, prompt
