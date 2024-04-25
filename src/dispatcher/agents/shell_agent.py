"""
shell agent中需求区分windows和linux
"""

import sys
import subprocess
from loguru import logger
from dispatcher.agents.agent import format_agent_result


@format_agent_result
def shell_agent(command: str, env_name: str = None):
    """
    windows 下执行command命令
    Args:
        command (str): windows shell command
        env_name (str, optional): conda环境，需要在用户提需求的时候进行指定
    """
    if sys.platform == 'win32':
        full_command = 'powershell.exe '
        command = command.replace('&&', ';')
        if env_name is not None and env_name != '':
            full_command += f'conda activate {env_name};'
        full_command = f'{full_command} {command}'
        rst = subprocess.run(full_command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        logger.debug(f'shell执行结果:{rst.stdout}')
        return rst.stdout
    elif sys.platform == 'linux':
        if env_name is not None and env_name != '':
            full_command += f' conda activate {env_name} && '
        full_command = f'{full_command} {command}'
        rst = subprocess.run(full_command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        logger.debug(f'shell执行结果:{rst}')
        return rst.stdout
