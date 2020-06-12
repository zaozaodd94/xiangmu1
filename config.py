import os
import time

import logging.handlers

BASE_ARITCAL_TITLE = "N95口罩特价_{}".format(time.strftime("%d%H%M%S"))
BASE_PATH = os.path.dirname(os.path.abspath("__file__"))

#日志配置的基础函数
def base_loger_config():
    #1.c创建日志器
    logger = logging.getLogger()
    #2.设置日志级别
    logger.setLevel(level=logging.INFO)
    #3创建处理器
    ls = logging.StreamHandler()
    lht = logging.handlers.TimedRotatingFileHandler(filename=BASE_PATH + "/log/test.log",when="midnight",interval=1,backupCount=2)
    #4,创建格式化器
    formatter = logging.Formatter(fmt="%(asctime)s-%(filename)s-%(levelno)s-%(lineno)s, %(message)s")
    formatter = logging.Formatter(fmt="%(asctime)s %(lecelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s")
    #5,将格式化器绑定到处理器
    ls.setFormatter(formatter)
    lht.setFormatter(formatter)
    #6将处理器添加到日志器中
    logger.addHandler(ls)
    logger.addHandler(lht)