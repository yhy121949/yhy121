# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : md5_tool.py
# Time       ：2021/4/15 14:25
# Author     ：xuepl
# version    ：python 3.7
"""
import hashlib


def md5(send_request, data):
    """
    md5加密
    :param send_request:
    :param data: 待加密数据
    :return:
    """
    if isinstance(data, str):
        return hashlib.md5(data.encode(encoding='UTF-8')).hexdigest()
    return
