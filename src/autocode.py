#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import argparse


from dispatcher.dispatcher import create_project


def parse_args(args=None, namespace=None):
    parser = argparse.ArgumentParser(description="自动编码系统")
    project = parser.add_subparsers(help="project")

    project_create = project.add_parser("project_create", aliases=['pc'], help="创建项目, 支持创建一般的项目继续创建")
    project_create.add_argument("-n", "--name", required=True, help="任务名称")
    project_create.add_argument("-p", "--path", required=True, help="项目存放路径")
    project_create.add_argument("-l", "--language", type=str, default='python', required=False,
                                help="主要编码语言")
    project_create.add_argument("-m", "--model_name", type=str, default='qwen', required=False, help="模型")
    project_create.add_argument("-s", "--search_engine", type=str, default='bing', required=False,
                                help="搜索引擎")
    project_create.add_argument("--env_name", type=str, required=False,
                                help="conda虚拟机环境")
    project_create.add_argument("--log_path", type=str, default='./logs', required=False,
                                help="日志路径, 默认在项目路径的logs目录")
    project_create.add_argument("--cache_path", type=str, default='./cache', required=False,
                                help="缓存路径, 便于中断项目的完善")
    project_create.add_argument("--project_subject", type=str, required=True,
                                help="项目主题内容")
    project_create.add_argument("--check_desc", type=str, required=True,
                                help="判断项目是否成功的描述")
    project_create.set_defaults(func=create_project)

    return parser.parse_args(args, namespace)


def main():
    # 解析参数
    args = parse_args()
    func = args.func
    args_dict = vars(args)
    del args_dict['func']

    # 启动函数
    func(**args_dict)


if __name__ == '__main__':
    main()
