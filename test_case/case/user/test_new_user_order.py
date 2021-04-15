# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : test_new_user_order.py
# Time       ：2021/4/15 11:46
# Author     ：xuepl
# version    ：python 3.7
"""
from common.send_request import SendRequest


def test_register():
    # 发送请求前的准备动作
    pre_process = [
        "$SET_VAR(phone,$PHONE()$)$",
        {"body": {
            "loginName": "$GET_VAR(phone)$"
        }}
    ]
    # 收到响应后的后置操作
    post_process = [
    ]
    SendRequest("test_case/json_data/user/register.json").send_request(post_process=post_process,
                                                                       pre_process=pre_process)


def test_login():
    # 发送请求前的准备动作
    pre_process = [
        {"body": {
            "loginName": "$GET_VAR(phone)$"
        }}
    ]
    # 收到响应后的后置操作
    post_process = [
        '$JSON_EXTRACTOR(token,$["data"] ,0)$'
    ]
    SendRequest("test_case/json_data/user/login.json").send_request(post_process=post_process,
                                                                    pre_process=pre_process)


def test_index_info():
    # 发送请求前的准备动作
    pre_process = [
    ]
    # 收到响应后的后置操作
    post_process = [
    ]
    SendRequest("test_case/json_data/get_index_info.json").send_request(post_process=post_process,
                                                                        pre_process=pre_process)
