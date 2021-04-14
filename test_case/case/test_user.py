# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : test_user.py
# Time       ：2021/4/8 8:48
# Author     ：xuepl
# version    ：python 3.7

"""
from common.send_request import SendRequest


def test_register_1():
    # 发送请求前的准备动作
    pre_process = [
        "$SET_VAR(name,1239)$",
        "$GET_VAR(name)$"
    ]
    # 收到响应后的后置操作
    post_process = [
        '$ASSERT_CONTAINS("resultCode": 200)$',
        "$JSON_EXTRACTOR(message,$.message,0)$"
    ]
    print(SendRequest("register.json").send_request(post_process=post_process, pre_process=pre_process).local_var)


def test_register_2():
    # 发送请求前的准备动作
    pre_process = ["$GET_VAR(name)$"]
    # 收到响应后的后置操作
    post_process = ['$ASSERT_CONTAINS("resultCode": 200)$', "$JSON_EXTRACTOR(message,$.message,0)$"]
    print(SendRequest("register.json").send_request(post_process=post_process, pre_process=pre_process).local_var)
