#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
基于参数，完成调度
"""

import os
from loguru import logger

from utils.comm_utils import get_full_path, find_params
from utils.logger import set_logger
from dispatcher.agents.agent import AgentFactory
from dispatcher.prompt.prompt_factory import prompt_pc, prompt_fix_error
from dispatcher.models.qwen_o import ModelQWenOffice
from dispatcher.models.parse_data import parse_answer
from dispatcher.global_params import global_params, plan_run_params


class Plan:
    """
    执行计划
    """
    def __init__(self, object_path: str, language: str, model, 
                 search_engine: str, env_name: str, cache_path: str,
                 strategy: str = 'c'):
        self.object_path = object_path
        self.language = language
        self.model = model
        self.search_engine = search_engine
        self.env_name = env_name
        self.cache_path = cache_path
        self.strategy = strategy

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
            for k, v in args.items():
                # 如果在参数值中存在变量(形式${param}),则判定名称是否在plan_run_params中，如果存在，则用值替换
                if '\$\{' in v:
                    params = find_params(v)
                    for p in params:
                        if p in plan_run_params:
                            v.replace('${'+p+'}', plan_run_params[p])
                    args[k] = v
            logger.debug(f'args:{args}')
            result = agent(**agent_info['args'])
            if 'check' in plan_info and result.get('status_code') == 0:
                # 如果当前agent执行正确，且有验证agent列表
                check_plans = plan_info['check']
                for check_plan in check_plans:
                    # 如果验证流程失败，则将失败信息返回
                    check_result = self._exec_plan(check_plan)
                    if result.get('status_code') != 0:
                        return check_result
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
                # 如果指定的output信息(存储的变量名称)，则将rst中的数据信息保存到plan_run_params中去
                if 'output' in plan_info:
                    output_name = plan_info['output']
                    plan_run_params[output_name] = rst
                return rst
            else:
                err_msg = result.get('err_msg')
                new_plan = {
                    'desc': plan_info['desc'],
                    'agent': plan_info['agent'],
                    'err_msg': err_msg,
                    'strategy': self.strategy
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
                   mode: str,
                   strategy: str,
                   scene: str,
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
    Args:
        name (str): 项目名称
        path (str): 项目存放路径
        strategy (str): 项目创建策略 c(完成优先)|e(效果优先) 默认c
        mode (str): 项目创建模式 conti(延续)|cover(重建)
        scene (str): 场景名称，create_project默认是pc
        language (str): 项目的主要编程语言
        model_name (str): 项目编码过程中使用的模型名称
        search_engine (str): 搜索引擎
        env_name (str): conda的env环境名称
        log_path (str): log日志存放的路径
        cache_path (str): cache文件存放的地址
        project_subject (str): 项目描述
        check_desc (str): 验证项目描述

    Raises:
        PermissionError: _description_
        Exception: _description_
    """
    if not os.path.exists(path):
        try:
            os.makedirs(path, exist_ok=True)
        except PermissionError:
            raise PermissionError("创建目录{path}权限不足")
        except Exception:
            raise Exception("创建目录{path}失败")
    
    path = path.replace('\\', '/')
    if not path.endswith('/'):
        path = path + '/'
    global_params['project_path'] = path
    logger.info(f'项目路径:{path}')

    # 格式化日志路径
    log_path = get_full_path(path, log_path)
    os.makedirs(log_path, exist_ok=True)
    
    # 配置日志
    set_logger(log_path)

    # 格式化缓存路径
    cache_path = get_full_path(path, cache_path)
    os.makedirs(cache_path, exist_ok=True)

    model = None
    if model_name == 'qwen-o':
        model = ModelQWenOffice()

    ##################################################
    logger.info('开始项目')
    # 开始执行
    extracts, prompt = prompt_pc(project_subject, check_desc=check_desc, strategy=strategy)
    # print(f'prompt:\n{first_prompt}')
    
    # 访问大模型，获取返回的结果
    answer = model.model(prompt)
    
    # 解析回答的内容
    key_infos = parse_answer(answer, titles=extracts)
    logger.info(f'解析answer结果, key_infos: {key_infos}')
    
    # cache
    cache_plans = []
    
    # 开始完成执行计划
    plan = Plan(object_path=path, language=language, model=model_name, cache_path=cache_path,
                 search_engine=search_engine, env_name=env_name, strategy=strategy)
    for k, v in key_infos.items():
        # 两个key, 一个是用需求，一个是效果验证
        logger.info(f'开始完成任务: {k}')
        for plan_dict in v:
            logger.info(f'执行计划详情: {plan_dict}')
            plan.exec(plan_dict)


