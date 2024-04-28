#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import argparse
from dotenv import load_dotenv

from dispatcher.config import config, get_config
from dispatcher.dispatcher import create_project


def parse_args(args=None, namespace=None):
    parser = argparse.ArgumentParser(description="自动编码系统")
    stage = parser.add_subparsers("stage", help="子场景")
    

    project_create = stage.add_parser("pc", aliases=['project_create'], help="创建项目, 支持创建一般的项目继续创建")
    project_create.add_argument("-n", "--name", required=True, help="任务名称")
    project_create.add_argument("-p", "--path", required=True, help="项目存放路径")
    project_create.add_argument("-d", "--develop_mode", required=True, default="default",
                                help="开发模型,在yaml中配置相关参数, default|dev|prod")
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
    
    develop_mode = args.develop_mode
    yaml_name = os.environ.get(args.stage)
    config(yaml_name, args.stage)
    if args.sub == 'project_create':
        args['strategy'] = get_config('strategy', args.stage, develop_mode)
        args['mode'] = get_config('mode', args.stage, develop_mode)
        args['model_name'] = get_config('model_name', args.stage, develop_mode)
        args['language'] = get_config('language', args.stage, develop_mode)
        args['search_engine'] = get_config('search_engine', args.stage, develop_mode)
        args['log_path'] = get_config('log_path', args.stage, develop_mode)
        args['env_name'] = get_config('env_name', args.stage, develop_mode)

    # 启动函数
    func(**args_dict)


if __name__ == '__main__':
    main()
