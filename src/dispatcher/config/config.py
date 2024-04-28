import os
import yaml
from loguru import logger

cfgs = {}

def config(yaml_filename: str, scene: str):
    """
    通过用户指定场景名称，到env中获取对应的yaml名称

    Args:
        yaml_filename (str): yaml名称
        scene (str): 场景名称
    Returns:
        _type_: yaml字典信息
    """
    # 单例
    if scene not in cfgs:
        # 获取当前脚本所在目录的绝对路径
        current_directory = os.path.dirname(os.path.realpath(__file__))
        
        # YAML文件名
        # yaml_filename = 'config.yaml'
        
        # 完整的YAML文件路径
        yaml_filepath = os.path.join(current_directory, yaml_filename)

        with open(yaml_filepath, "r", encoding='utf-8') as f:
            try:
                # 使用yaml.safe_load()读取YAML内容
                cfg = yaml.safe_load(f)
                cfgs[scene] = cfg
                return cfg
            except yaml.YAMLError as e:
                print(e)
                return None
    else:
        return cfgs[scene]

def get_config(config_name: str, scene: str, develop_mode: str = 'default'):
    """
    获取配置，如果develop_mode不为default，获取config内容失败，需要再从default中获取一次
    Args:
        config_name (str): 需要获取的配置名称
        scene (str): 场景名称
        develop_mode (str, optional): 开发模式，一共有三种，default, dev, prod. Defaults to 'default'.
    Returns:
        str: 获取配置项的内容，如果没有获取成功，则返回None
    """
    if scene not in cfgs:
        logger.error(f'场景: {scene} 未初始化')
        return None
    if develop_mode not in cfgs[scene]:
        logger.error(f'develop_mode: {develop_mode} 不在Yaml配置')
        return None
    mode_dict = cfgs[scene][develop_mode]
    value = mode_dict.get(config_name, None)
    if value is None and develop_mode != 'default':
        default_dict = cfgs[scene]['default']
        value = default_dict.get(config_name, None)
    return value
        
    