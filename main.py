# -*- coding: UTF-8 -*-

from thinkutils.log.log import g_logger
from thinkutils.datetime.datetime_utils import *

g_logger.info("Hello World")
g_logger.info(today())
g_logger.info(get_current_time_str())