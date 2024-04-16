"""
通过执行str完成python代码执行，存在如下三种情况
1. 执行某段代码，需要传入参数
"""

from pyparsing import Any

from src.logs.ansi import SGR
from src.logs.logger import logger
from src.dispatcher.agents import Agents, AgentFactory


class PythonAgents(Agents):
    """
    python agent集合
    类似Python REPL(Read-Eval-Print-Loop)
    
    参考ptpython
    https://github.com/prompt-toolkit/ptpython/blob/master/ptpython/repl.py#L90
    """
    def __init__(self):
        AgentFactory.register_agent('run_python', self.run_python)
        AgentFactory.register_agent('merge_code', self.merge_code)

    def run_python(self, code, return_keys, **kwargs: Any):
        """
        code: 需要执行的python代码
        return_keys: 需要返回的变量名称列表
        kwargs: python代码执行中需要传入的参数对{key:value}的形式

        使用方式，详见测试用例test_python.py
        """
        params = dict(kwargs) 
        exec(code, params)
        result = {}
        if return_keys and len(return_keys) > 0:
            for k in return_keys:
                result[k] = params[k]
        return result
    
    def merge_code(self, code, merge_file_path):
        """
        将code写入merge_file_path对应的文件中
        
        主要判定下引入是否有重复
        """
        with open(merge_file_path, 'w') as merge_file:
            merge_file.write(code)