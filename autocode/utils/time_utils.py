import time


def format_time(formatter: str = '%Y-%m-%d %H:%M:%S',
                timestamp: time.struct_time = None):
    """
    将时间戳进行格式化
    Args:
        formatter (str): 日期格式
        timestamp (_type_, optional): 时间戳.
    """
    if timestamp is None:
        timestamp = time.localtime()
    return time.strftime(formatter, timestamp)
