"""
shell agent中需求区分windows和linux
"""


import subprocess
from agent import format_agent_result


@format_agent_result
def windows_shell_agent(command: str, env_name: str = None):
    """
    windows 下执行command命令
    Args:
        command (str): windows shell command
        env_name (str, optional): conda环境，需要在用户提需求的时候进行指定
    """
    full_command = 'powershell.exe '
    if env_name is not None:
        full_command += f'conda activate {env_name};'
    full_command = f'{full_command} {command}'
    subprocess.run(full_command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)


@format_agent_result

def linux_shell_agent(command: str, env_name: str = None):
    """
    windows 下执行command命令
    Args:
        command (str): windows shell command
        env_name (str, optional): conda环境，需要在用户提需求的时候进行指定
    """
    if env_name is not None:
        full_command += f' conda activate {env_name} && '
    full_command = f'{full_command} {command}'
    subprocess.run(full_command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
