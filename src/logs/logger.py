import os
import re
from loguru import logger

log = logger.add('runtime_{time}.log', rotation='00:00')
