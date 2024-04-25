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
from dispatcher.prompt.prompt_factory import prompt_pc, prompt_fix_error
from dispatcher.models.qwen_o import ModelQWenOffice
from dispatcher.models.parse_data import parse_answer


class Plan:
    """
    执行计划
    """
    def __init__(self, object_path: str, language: str, model, 
                 search_engine: str, env_name: str):
        self.object_path = object_path
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
        agent = AgentFactory.get_agent(agent_name)['func']
        if 'args' in agent_info:
            args = dict(agent_info['args'])
            # args = dict(agent_info['args'])
            logger.debug(f'args:{args}')
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
                logger.info(f'执行结果: {rst}')
                return rst
            else:
                err_msg = result.get('err_msg')
                new_plan = {
                    'desc': plan_info['desc'],
                    'agent': plan_info['agent'],
                    'err_msg': err_msg
                }
                extracts, prompt = prompt_fix_error(**new_plan)
                logger.info(f'执行失败，重新构建Prompt: {prompt}')
                answer = self.model(prompt)
    
                # 解析回答的内容
                new_plan_info = parse_answer(answer, titles=extracts)
                print(f'解析answer结果, new_plan_info: {new_plan_info}')
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
    if model_name == 'qwen-o':
        model = ModelQWenOffice()

    ##################################################
    logger.info('开始项目')
    # 开始执行
    extracts, prompt = prompt_pc(project_subject, check_desc=check_desc)
    # print(f'prompt:\n{first_prompt}')
    
    # 访问大模型，获取返回的结果
    answer = model.model(prompt)
    
    # 解析回答的内容
    key_infos = parse_answer(answer, titles=extracts)
    logger.info(f'解析answer结果, key_infos: {key_infos}')
    
    # 开始完成执行计划
    plan = Plan(object_path=path, language=language, model=model_name, 
                 search_engine=search_engine, env_name=env_name)
    for k, v in key_infos.items():
        # 两个key, 一个是用需求，一个是效果验证
        logger.info(f'开始完成任务: {k}')
        for plan_dict in v:
            logger.info(f'执行计划详情: {plan_dict}')
            plan.exec(plan_dict)


