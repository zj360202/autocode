from abc import ABC, abstractmethod
from typing import Any


class Agents(ABC):
    @property       # 必须写在上面，不然在运行的时候会报错
    @abstractmethod
    def type_name(self):
        """设定类型"""


class AgentFactory:
    
    agent_fun_mapping = {}
    
    @staticmethod
    def register_agent(name, fun):
        """每一个agent是一个agent类中的一个方法"""
        AgentFactory.agent_fun_mapping[name] = fun
    
    @staticmethod
    def get_agent(name):
        return AgentFactory.agent_fun_mapping[name]
    
    @staticmethod
    def exec_agent(name, agent_args):
        """执行agent"""
        return AgentFactory.agent_fun_mapping[name](agent_args)
