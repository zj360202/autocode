#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
基于参数，完成调度
"""

import os
from src.utils.comm_utils import get_full_path
from src.dispatcher.agents.agent import AgentFactory


class Plan:
    """
    执行计划
    """
    def __init__(self, agents: list, level: int = 0):
        self.agents = agents
        self.level = level

    def exec(self):
        for agent in self.agents:
            AgentFactory.exec_agent(**agent)

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




