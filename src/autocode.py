#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import argparse
from dotenv import load_dotenv

from dispatcher.config.config import config, get_config
from dispatcher.dispatcher import create_project


def parse_args(args=None, namespace=None):
    parser = argparse.ArgumentParser(description="自动编码系统")
    scene = parser.add_subparsers(dest="scene", help="子场景")
    

    project_create = scene.add_parser("pc", aliases=['project_create'], help="创建项目, 支持创建一般的项目继续创建")
    project_create.add_argument("-n", "--name", required=True, help="任务名称")
    project_create.add_argument("-p", "--path", required=True, help="项目存放路径")
    project_create.add_argument("-d", "--develop_mode", default="default",
                                help="开发阶段,在yaml中配置相关参数, default|dev|prod")
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
    del args_dict['develop_mode']
    
    yaml_name = os.environ.get(args.scene)
    config(yaml_name, args.scene)
    
    # 获取不同场景下的所有参数
    if args.scene == 'pc':
        args_dict['strategy'] = get_config('strategy', args.scene, develop_mode)
        args_dict['mode'] = get_config('mode', args.scene, develop_mode)
        args_dict['model_name'] = get_config('model_name', args.scene, develop_mode)
        args_dict['language'] = get_config('language', args.scene, develop_mode)
        args_dict['search_engine'] = get_config('search_engine', args.scene, develop_mode)
        args_dict['log_path'] = get_config('log_path', args.scene, develop_mode)
        args_dict['cache_path'] = get_config('cache_path', args.scene, develop_mode)
        args_dict['env_name'] = get_config('env_name', args.scene, develop_mode)

    print(f'args_dict:{args_dict}')
    # 启动函数
    func(**args_dict)


if __name__ == '__main__':
    main()
