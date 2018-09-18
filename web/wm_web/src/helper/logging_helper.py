#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import  logging.config
import sys
import os
import re

'''
logging helper
'''
class LoggingHelper:

    @staticmethod
    def get_logger(sys):

        logging.config.fileConfig('../wm_web/src/helper/logging.conf')
        logger = logging.getLogger('simpleExample')
        #logger_file = logging.getLogger('main')
        fmt_str = '%(asctime)s[level-%(levelname)s][%(name)s]:%(message)s'
        # 初始化
        logging.basicConfig()
        # 创建TimedRotatingFileHandler处理对象
        # 间隔1(D)创建新的名称为autotest%Y%m%d_%H%M%S.log的文件，并一直占用myLog文件。
        log_path=os.path.join(os.pardir,"log",sys)
        if os.path.exists(log_path):
            pass
        else:
            os.makedirs(log_path)

        log_path =os.path.join(log_path, 'webautotest')
        fileshandle = logging.handlers.TimedRotatingFileHandler(log_path, when='D', interval=1, backupCount=20)
        # 设置日志文件后缀，以当前时间作为日志文件后缀名。
        fileshandle.suffix = '%Y%m%d.log'
        # 设置日志输出级别和格式
        fileshandle.setLevel(logging.DEBUG)
        formatter = logging.Formatter(fmt_str)
        fileshandle.setFormatter(formatter)
        # 添加到日志处理对象集合
        logger_file =logging.getLogger('')
        logger_file.addHandler(fileshandle)
        return logger_file
