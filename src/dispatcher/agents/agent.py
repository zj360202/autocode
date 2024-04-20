import inspect
from abc import ABC, abstractmethod

from utils.comm_utils import agent_desc



def format_agent_result(agent_func):
    # 将agent的返回值格式化
    def wrapper():
        try:
            rst = agent_func()
            result = {'status_code': 0, 'data': rst}
        except Exception as e:
            result = {'status_code': 1, 'err_msg': str(e)}
        return result



class AgentFactory:
    agent_func_mapping = {}

    @staticmethod
    def register_agent(name, func):
        """每一个agent是一个agent类中的一个方法"""
        if name in AgentFactory.agent_func_mapping:
            raise ValueError(f'agent: {name} 已经被定义过了')

        # 获取函数的参数信息
        func_desc, args_desc = agent_desc(name, func)

        # 封装desc
        desc = f'{name}: {func_desc}\n'
        for arg_desc in args_desc:
            desc += f'\t{arg_desc}\n'

        # 注册agent
        AgentFactory.agent_func_mapping[name] = {'desc': desc, 'func': func}

    @staticmethod
    def get_agent(name):
        if name not in AgentFactory.agent_func_mapping:
            raise ValueError(f'agent: {name} 未被定义')
        return AgentFactory.agent_func_mapping[name]

    @staticmethod
    def exec_agent(name, agent_args):
        """执行agent"""
        if name not in AgentFactory.agent_func_mapping:
            raise ValueError(f'agent: {name} 未被定义')
        return AgentFactory.agent_func_mapping[name]['func'](agent_args)

    @staticmethod
    def agent_mapping():
        return AgentFactory.agent_func_mapping
