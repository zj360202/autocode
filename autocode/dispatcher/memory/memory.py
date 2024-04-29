"""
主要是三种内存类型
1. 基于完全内存
2. 基于redis内存db
3. 基于index的数据库
"""
from abc import ABC, abstractmethod


class MemoryBase(ABC):
    """
    基于Session的数据保存机制
    1. 创建session
    2. 添加数据, 并判定是否进入死循环
    3. 给定执行计划，判定是否重复

    x. 过期数据删除
    """

    @abstractmethod
    def create_session(self) -> str:
        """创建session"""

    @abstractmethod
    def add_data(self, session_id, data) -> dict:
        """
        将数据添加到对应session中
        data: {
            type: 可以取值 model|tool
            name: model取值model name, agent取值tool name
            input: 传入的完整内容
            input_params: 传入的内容中，参数部分
            output: 输出结果
        }
        返回结果格式
        result: {
            is_
        }
        """

    @abstractmethod
    def is_repeat_plan(self, session_id, data) -> bool:
        """
        给定执行计划，判定是否重复
        data: {
            type: 可以取值 model|tool
            name: model取值model name, agent取值tool name
            input: 传入的完整内容
            input_params: 传入的内容中，参数列表
        }
        在type, name相同的情况下，主要判定input_params
        """

    @abstractmethod
    def del_session(self, session_id):
        """对于过期数据，如果需要删除的，则进行删除"""


memory_data = {}


class Memory(MemoryBase):
    def create_session(self) -> str:
        """
        创建session_id放入到内存的chat中
        session_id = (max_index+1)前面补零，补齐8位数
        将最大索引放入到max_index中，以便后续进行创建的时候，可以轻松获取

        插入的时候，判定是否已经存在，如果已经存在，则重新获取max_index
        然后通过session_id公式创建，插入的时候，需要再次判定
        """
        if 'chat' not in memory_data:
            memory_data['chat'] = {}
            memory_data['chat']['max_index'] = 0
        max_index = memory_data['chat']['max_index'] + 1
        session_id = str(max_index).zfill(8)
        while session_id in memory_data['chat']:
            max_index = memory_data['chat']['max_index'] + 1
            session_id = str(max_index).zfill(8)
        memory_data['chat']['max_index'] = max_index
        memory_data['chat'][session_id] = []
        return session_id

    def add_data(self, session_id, data) -> dict:
        """
        将数据添加到对应session中
        data: {
            type: 可以取值 model|tool
            name: model取值model name, agent取值tool name
            plan: plan内容
            input: 传入的完整内容
            input_params: 传入的内容中，参数部分
            output: 输出结果
        }
        1. 先判定是否重复
        2. 判定
        """
        is_repeat = self.is_repeat_plan(session_id, data)
        result = {
            'is_repeat': is_repeat,
            'output': None
        }

    def is_repeat_plan(self, session_id, data) -> bool:
        """
        给定执行计划，判定是否重复
        data: {
            type: 可以取值 model|tool
            name: model取值model name, agent取值tool name
            plan: plan内容
            input: 传入的完整内容
            input_params: 传入的内容中，参数列表
        }
        在type, name相同的情况下，主要判定plan
        """
        session_data = memory_data['chat'][session_id]
        for s_data in session_data:
            if (s_data['type'] == data['type']
                    and s_data['name'] == data['name']
                    and len(s_data['plan']) == len(data['plan'])):
                return True
        return False

    def del_session(self, session_id):
        """对于过期数据，如果需要删除的，则进行删除"""
        del memory_data['chat'][session_id]
