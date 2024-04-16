"""
通过执行str完成python代码执行，存在如下三种情况
1. 执行某段代码，需要传入参数
"""

from pyparsing import Any

from src.logs.ansi import SGR
from src.logs.logger import logger
from src.tools.tool import Tool


def input_params(python_code: str,
                 return_keys: list,
                 **kwargs: Any):
    """
    python_code: 需要执行的python代码
    return_keys: 需要返回的变量名称列表
    kwargs: python代码执行中需要传入的参数对{key:value}的形式

    使用方式，详见测试用例test_python.py
    """
    params = dict(kwargs)
    log_content = f'python_code:\n```python\n{python_code}\n```\n执行参数:{params}\n返回列表:{return_keys}'
    exec(python_code, params)
    result = []
    if return_keys and len(return_keys) > 0:
        result = [(rk, params[rk]) for rk in return_keys]
    log_content += f'\n执行结果:{result}'
    logger.info(log_content, 'python tools执行内容', title_color=SGR.BLUE_BG)
    return result


class PythonTool(Tool):
    """
    类似Python REPL(Read-Eval-Print-Loop)
    
    参考ptpython
    https://github.com/prompt-toolkit/ptpython/blob/master/ptpython/repl.py#L90
    """

    @property
    def name(self):
        return 'python'

    def _run(self,
             commands: str,
             return_keys: list,
             **kwargs: Any):
        return input_params(commands, return_keys, kwargs)
        
    async def _arun(self,
                    commands: str,
                    return_keys: list,
                    **kwargs: Any):
        return input_params(commands, return_keys, kwargs)
