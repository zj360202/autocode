#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import argparse
from dotenv import load_dotenv


from dispatcher.dispatcher import create_project


def parse_args(args=None, namespace=None):
    parser = argparse.ArgumentParser(description="自动编码系统")
    project = parser.add_subparsers(help="project")

    default_s = os.environ.get('STRATEGY', 'c')
    default_m = os.environ.get('MODE', 'conti')
    default_l = os.environ.get('LANGUAGE', 'python')
    default_se = os.environ.get('SEARCH_ENGINE', 'bing')
    default_llm = os.environ.get('LLM', 'qwen-o')
    default_log = os.environ.get('LOG_PATH', './logs')
    default_cache = os.environ.get('CACHE_PATH', './cache')

    project_create = project.add_parser("project_create", aliases=['pc'], help="创建项目, 支持创建一般的项目继续创建")
    project_create.add_argument("-n", "--name", required=True, help="任务名称")
    project_create.add_argument("-p", "--path", required=True, help="项目存放路径")
    project_create.add_argument("-s", "--strategy", type=str, default=default_s, help="项目创建策略 c(完成优先)|e(效果优先) 默认c")
    project_create.add_argument("-m", "--mode", type=str, default=default_m, help="项目创建模式 conti(延续)|cover(重建)")
    project_create.add_argument("-l", "--language", type=str, default=default_l, required=False,
                                help="主要编码语言(默认python)")
    project_create.add_argument("--model_name", type=str, default=default_llm, required=False, help="模型(默认qwen-o)")
    project_create.add_argument("--search_engine", type=str, default=default_se, required=False,
                                help="搜索引擎(默认bing)")
    project_create.add_argument("--env_name", type=str, required=False,
                                help="conda虚拟机环境")
    project_create.add_argument("--log_path", type=str, default=default_log, required=False,
                                help="日志路径, 默认./logs")
    project_create.add_argument("--cache_path", type=str, default=default_cache, required=False,
                                help="缓存路径, 默认./cache")
    project_create.add_argument("--project_subject", type=str, required=True,
                                help="项目主题内容")
    project_create.add_argument("--check_desc", type=str, required=True,
                                help="判断项目是否成功的描述")
    project_create.set_defaults(func=create_project)

    return parser.parse_args(args, namespace)


def main():
    # 加载环境变量
    load_dotenv()
    
    # 解析参数
    args = parse_args()
    func = args.func
    args_dict = vars(args)
    del args_dict['func']

    # 启动函数
    func(**args_dict)


if __name__ == '__main__':
    main()
