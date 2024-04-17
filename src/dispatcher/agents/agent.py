from abc import ABC, abstractmethod


class Agents(ABC):
    @property       # 必须写在上面，不然在运行的时候会报错
    @abstractmethod
    def desc(self):
        """设定类型"""


class AgentFactory:
    
    agent_fun_mapping = {}
    
    @staticmethod
    def register_agent(name, desc, fun):
        """每一个agent是一个agent类中的一个方法"""
        if name in AgentFactory.agent_fun_mapping:
            raise ValueError(f'agent: {name} 已经被定义过了')
        AgentFactory.agent_fun_mapping[name] = {'desc': desc, 'fun': fun}
    
    @staticmethod
    def get_agent(name):
        if name not in AgentFactory.agent_fun_mapping:
            raise ValueError(f'agent: {name} 未被定义')
        return AgentFactory.agent_fun_mapping[name]
    
    @staticmethod
    def exec_agent(name, agent_args):
        """执行agent"""
        if name not in AgentFactory.agent_fun_mapping:
            raise ValueError(f'agent: {name} 未被定义')
        return AgentFactory.agent_fun_mapping[name]['fun'](agent_args)

    @staticmethod
    @staticmethod
    def agent_mapping():
        return AgentFactory.agent_fun_mapping