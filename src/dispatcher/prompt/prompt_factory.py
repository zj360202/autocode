from .prompt import prompt_agents, prompt_user_demand_create_project_input
from .prompt import prompt_user_demand_create_project_output, prompt_demand_analyse_input
from .prompt import prompt_python_code_input, prompt_python_code_output, prompt_error_fix_input
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

def prompt_pc(project_subject: str, check_desc: str):
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
    
    # 配置输出格式化
    extracts += prompt_user_demand_create_project_output['extract']
    prompt += prompt_user_demand_create_project_output['prompt']
    
    return extracts, prompt

def prompt_fix_error(desc: str, agent: str, err_msg: str):
    # 开始初始化prompt
    extracts = prompt_error_fix_input['extract']
    prompt = prompt_error_fix_input['prompt'].format(desc=desc, agent=agent, err_msg=err_msg)
    
    return extracts, prompt
