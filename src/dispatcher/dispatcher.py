#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
基于参数，完成调度
"""

import os
from src.utils.comm_utils import get_full_path


class Agent:
    agent_type_mapping = {
        'model_qwen': 'model',
        'bing_search': 'web_search',
        'exec_python': 'python',
        'pip_install': 'shell',

    }
    type_fun_mapping = {
        'model': '',
        'web_search': '',
        'python': '',
        'shell': '',
    }

    def __init__(self, name: str, agent_args: dict, desc: str = None):
        """
        执行代理，每一个代理只能是一个action执行
        """
        self.name = name
        self.agent_args = agent_args
        self.desc = desc

    def exec(self):
        agent_type = self.agent_type_mapping.get(self.name)
        if agent_type is not None:
            agent = self.type_fun_mapping[agent_type]
            result = agent(self.name, **self.agent_args)
            return result
        else:
            # 如果出错，一般是需要让模型重新更新这一块的描述的
            pass


class Plan:
    """
    执行计划
    """
    def __init__(self, agents: list, level: int = 0):
        self.agents = agents
        self.level = level

    def exec(self):
        for agent in self.agents:
            agent.exec()

    def cache(self):
        pass

    def check(self):
        pass


def create_project(name: str,
                   path: str,
                   language: str,
                   model: str,
                   search_engine: str,
                   log_path: str,
                   cache_path: str,
                   project_subject: str,
                   check_desc: str):
    """
    创建项目
    """
    if not os.path.exists(path):
        try:
            os.makedirs(path, exist_ok=True)
        except PermissionError:
            raise PermissionError("创建目录{path}权限不足")
        except Exception:
            raise Exception("创建目录{path}失败")

    # 格式化日志路径
    log_path = get_full_path(log_path, path)
    os.makedirs(log_path, exist_ok=True)

    # 格式化缓存路径
    cache_path = get_full_path(cache_path, path)
    os.makedirs(cache_path, exist_ok=True)

    ##################################################
    # 开始执行
    first_prompt = ""




