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
from dispatcher.prompt.prompt import prompt_user_demand_create_project_output, prompt_error_fix_input
from dispatcher.models.qwen import ModelQWen
from dispatcher.models.parse_data import parse_answer


class Plan:
    """
    执行计划
    """
    def __init__(self, language: str, model, 
                 search_engine: str, env_name: str):
        self.language = language
        self.model = model
        self.search_engine = search_engine
        self.env_name = env_name

        # 执行步骤中的参数
        self.max_loop = 10  # 如果执行失败，最大重试次数

    def _exec_plan(self, plan_info: dict):
        """
        执行计划

        1. 获取执行计划的描述 key:desc
        2. 获取执行计划的agent信息 key: agent
        """
        agent_info = plan_info.get('agent')
        agent_name = agent_info['name']
        agent = AgentFactory.get_agent(agent_name)
        if 'args' in agent_info:
            result = agent(**agent_info['args'])
        else:
            result = agent()
        return result


    def exec(self, plan_info: dict):
        loop = 0
        while loop < self.max_loop:
            loop += 1
            result = self._exec_plan(plan_info)
            if result.get('status_code') == 0:
                # 执行成功
                rst = result.get('data')
                return rst
            else:
                err_msg = result.get('err_msg')
                new_plan = {
                    'desc': plan_info['desc'],
                    'agent': plan_info['agent'],
                    'err_msg': err_msg
                }
                prompt = prompt_error_fix_input.format(**new_plan)
                answer = self.model(prompt)
    
                # 解析回答的内容
                new_plan_info = parse_answer('error_fix', answer)
                return self.exec(new_plan_info)

    def cache(self):
        pass


def create_project(name: str,
                   path: str,
                   language: str,
                   model_name: str,
                   search_engine: str,
                   env_name: str,
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

    model = None
    if model_name == 'qwen':
        model = ModelQWen()

    ##################################################
    # 开始执行
    first_prompt = prompt_user_demand_create_project_input.format(demand=project_subject,
                                                                  check_desc=check_desc,
                                                                  prompt_agents=prompt_agents)
    first_prompt += prompt_user_demand_create_project_output
    # print(f'prompt:\n{first_prompt}')
    
    # 访问大模型，获取返回的结果
    answer = model.model(first_prompt)
    
    # 解析回答的内容
    key_infos = parse_answer('pc', answer)
    
    # 1. 创建项目目录结构
    
    # 2. 完成项目执行计划
    plans = key_infos['plans']
    
    # 3. 完成验证执行计划
    check_plans = key_infos['check_plans']
    #
    # # 解析回答的内容
    #
    # is_continue = True
    # while is_continue:
    #     pass



