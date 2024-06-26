################################################################################
###############                不同场景的流程拆解                 ###############
################################################################################


################################################################################
### 爬虫
################################################################################
scene_crawling_prompt = {
    # 需要人工补充的信息
    'inputs': ['target_url', 'table_tr_css', 'item_css_list', 'next_page_css', 'save_info', 'mapping_info'],
    'prompt':"""
现有crawling.py, 包含如下函数
{fun_desc_list}

爬虫需求步骤说明如下:
1. 打开浏览器
2. 访问{target_url}
3. 获取页面的表格行列表元素, css: {table_tr_css}
4. 遍历所有的行，并获取每一行的列数据，列名称列表: {item_css_list}
5. 将当前页面数据进行保存，保存信息是: {save_info}, 字段映射信息: {mapping_info}
6. 判定是否有下一页，如果有下一页，则点击，并返回步骤3
7. 如果没有下一页，则将退出
    """
}

################################################################################
### web接口
################################################################################
scene_web_interface_prompt = {
    # 需要人工补充的信息
    'inputs': ['interface_infos'],
    'prompt':"""
web接口需求步骤说明如下:
1. 使用flask开发，并给出flask pip安装命令
2. 生成interface.py, 包含flask使用的基本代码
3. 遍历{interface_infos}中的信息，生成按要求的接口名称，参数和返回信息，代码实现部分交给大模型按需求进行完成
    """
}


################################################################################
### web项目 需要vue和python配合
################################################################################
scene_web_prompt = {
    # 需要人工补充的信息
    'inputs': ['interface_infos'],
    'prompt':"""
web接口需求步骤说明如下:
1. 使用flask开发，并给出flask pip安装命令
2. 生成interface.py, 包含flask使用的基本代码
3. 遍历{interface_infos}中的信息，生成按要求的接口名称，参数和返回信息，代码实现部分交给大模型按需求进行完成
    """
}

