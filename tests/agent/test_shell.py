
"""
通过执行str完成python代码执行
1. 执行某段代码，需要传入参数，并且获取返回值
"""
from unittest import TestCase
from loguru import logger

from dispatcher.agents.shell_agent import windows_shell_agent


class TestShell(TestCase):
    def test_windows_shell(self):
        """
        通过代码定义的函数，只能算做局部函数，在当前方法的外面是无法使用的
        """
        command = "C:\Windows\System32\calc.exe"
        result = windows_shell_agent(command)
        logger.debug(f'result:{result}')
