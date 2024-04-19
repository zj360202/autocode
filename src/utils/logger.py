import os
import re
from loguru import logger

def set_logger(log_path: str='.'):
    logger.add(log_path+'/runtime_{time}.log', rotation='00:00')
