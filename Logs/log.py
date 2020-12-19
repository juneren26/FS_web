# coding=utf-8
'''
@Time   :2020/12/11 11:54
@Author :六月
@Email  :juneren26@gmail.com
@File   :log.py
@IDE    :PyCharm
'''
import logging
import os
import time
# 设置日志绝对路径
curPath = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

class Logger():
    def get_logger(self):
        # 创建日志对象
        logger = logging.getLogger('logger')
        logger.setLevel(logging.DEBUG)
        if not logger.handlers:
            sh = logging.StreamHandler()
            now = time.strftime('%Y_%m_%d %H_%M_%S')
            fh = logging.FileHandler('{}/logs/{}_logs.log'.format(curPath,now),encoding='utf-8')
            fmt = logging.Formatter(fmt='[%(filename)s]:%(asctime)s - %(levelname)s - %(message)s')
            sh.setFormatter(fmt)
            sh.setLevel(logging.DEBUG)
            fh.setFormatter(fmt)
            fh.setLevel(logging.DEBUG)
            logger.addHandler(sh)
            logger.addHandler(fh)
        return logger
