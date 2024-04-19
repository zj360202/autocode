#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
基于参数，完成调度
"""

import os
from loguru import logger

from utils.comm_utils import get_full_path
from utils.logger import set_logger
from dispatcher.agents.agent import AgentFactory
from dispatcher.prompt.prompt import prompt_user_demand_create_project_input, prompt_agents
from dispatcher.prompt.prompt import prompt_user_demand_create_project_output
from dispatcher.models.qwen import ModelQWen


class Plan:
    """
    执行计划
    """
    def __init__(self, agents: list, level: int = 0):
        self.agents = agents
        self.level = level

    def exec(self):
        max_loop, loop = 10, 0
        run_flag = True
        for agent in self.agents:
            # 依次执行agent，如果在执行过程中出错，则直接将输入和错误信息通过模型进行优化
            while run_flag or loop < max_loop:
                try:
                    AgentFactory.exec_agent(**agent)
                    run_flag = True
                    loop = 0
                except Exception as e:
                    logger.error(f"")
                    run_flag = False
                    loop += 1
                    # 判定就code执行还是shell执行
                    prompt = f'{agent.args}'
                    params = {'name': 'qwen', 'args':{}}
                    result = AgentFactory.exec_agent(**params)
                    agent.args['prompt'] = result

    def cache(self):
        pass

    def check(self):
        pass


def create_project(name: str,
                   path: str,
                   language: str,
                   model_name: str,
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
    
    # 配置日志
    set_logger(log_path)

    # 格式化缓存路径
    cache_path = get_full_path(cache_path, path)
    os.makedirs(cache_path, exist_ok=True)

    # model = None
    # if model_name == 'qwen':
    #     model = ModelQWen()

    ##################################################
    # 开始执行
    first_prompt = prompt_user_demand_create_project_input.format(demand=project_subject,
                                                                  check_desc=check_desc,
                                                                  prompt_agents=prompt_agents)
    first_prompt += prompt_user_demand_create_project_output
    print(f'prompt:\n{first_prompt}')
    # answer = model.model(first_prompt)
    #
    # # 解析回答的内容
    #
    # is_continue = True
    # while is_continue:
    #     pass



