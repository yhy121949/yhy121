# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : log.py
# Time       ：2021/4/7 17:42
# Author     ：xuepl
# version    ：python 3.7
"""

import logging
import os
from logging.handlers import TimedRotatingFileHandler

'''
封装log方法
'''
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)

root_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../logs/")
if not os.path.exists(root_path):
    os.makedirs(root_path)
handler = TimedRotatingFileHandler(root_path + 'info.log', when='d', interval=1, backupCount=30, encoding='utf-8')
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

handler2 = TimedRotatingFileHandler(root_path + 'error.log', when='d', interval=1, backupCount=30, encoding='utf-8')
handler2.setLevel(logging.ERROR)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler2.setFormatter(formatter)
logger.addHandler(handler2)

handler3 = logging.StreamHandler()
handler3.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler3.setFormatter(formatter)
logger.addHandler(handler3)


def info(msg):
    logger.info(msg)


def debug(msg):
    logger.debug(msg)


def warning(msg):
    logger.warning(msg)


def error(msg):
    logger.error(msg)


def critical(msg):
    logger.critical(msg)
