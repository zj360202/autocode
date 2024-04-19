
"""
通过执行str完成python代码执行
1. 执行某段代码，需要传入参数，并且获取返回值
"""
from unittest import TestCase

from dispatcher.agents.python_agent import run_python


class TestPython(TestCase):
    def test_run_python(self):
        """
        通过代码定义的函数，只能算做局部函数，在当前方法的外面是无法使用的
        """
        python_code = """
class Code():
    def __init__(self):
        print("okok=============")
def test(a):
    # print("函数内的locals：", locals())
    c = Code()
    return a+1
# print("函数外的locals：", locals())
a = test(a)
b = a+1
        """
        return_keys = ['a', 'b']
        result = run_python(python_code, return_keys=return_keys, args_dict={'a': 8})
        print(result)   # [('a', 9), ('b', 10)]
