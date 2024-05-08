"""
记录一些通用prompt
"""


###################################################################################
# agent列表
prompt_agents = {
    'extract': [],
    'prompt':"""
描述规范是:
agent_name: agent_desc
    arg1(arg_type): arg1_desc
    arg2(arg_type): arg2_desc
agent列表如下，
{agent_infos}

请给出对于用户需求和验证效果描述的执行计划，给出的计划必须满足如下要求：
1. 对自己的能力与行为的匹配进行review
2. 大局观与自我反思
3. 长期记忆对决策动作进行优化
4. 尽可能高效率的使用较少的动作来完成任务
5. 对于同一个任务，可以通过多种agent完成，如何让算法能够选择最好的解决方法
    比如：获取当期日期，可以通过python，web搜索，shell等，选择哪种最合适
"""
}

###################################################################################
# 根据用户需求+搜索结果，得到项目的完成计划
prompt_demand_to_plan = {
    'extract': [],
    'prompt': """
用户需求:
{demand}

搜索结果(下面虚线中的内容全部是搜索结果):
--------------------------------
{search_info}
--------------------------------

通过上述内容，请给出完成用户需求的执行计划，每一个执行计划以1.,2.开始:
"""
}

###################################################################################
# 用户需求
prompt_user_demand_create_project_input = {
    'extract': [],
    'prompt':"""
用户需求: 
{demand}

验证项目效果描述:
{check_desc}
"""
}

# 爬虫项目分析, 直接获取页面数据
prompt_crawling_analyse = {
    'extract': [],
    'prompt':"""
用DrissionPage完成爬虫功能:
1. 打开浏览器
2. 访问url:{url}
3. 
"""
}

# 爬虫项目分析, 通过db数据生成url进行访问，然后进行爬取

###################################################################################
# python代码生成
# demand需求：来自用户或是通过模型生成的计划描述
prompt_python_code_input = {
    'extract': [],
    'prompt':"""
使用python, 完成需求: {demand}
"""
}

prompt_python_code_output = {
    'extract': ['pip安装内容', 'import相关内容', 'python代码'],
    'prompt':"""
python 代码生成，返回格式化如下，下面{content}中是需要生成和替换的内容
pip安装内容如下:
```shell
{content}
```

import相关内容如下:
```python
{content}
```

python代码内容如下:
```python
{content}
```
"""
}

###################################################################################
# 执行错误后，让模型修正
prompt_error_fix_input = {
    'extract': [],
    'prompt':"""
需求描述: 
{demand_desc}

执行内容, agent信息:
{agent_info}

执行错误如下:
```shell
{err_msg}
```
"""
}

