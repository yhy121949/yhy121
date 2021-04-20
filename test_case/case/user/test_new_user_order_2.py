# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : test_new_user_order.py
# Time       ：2021/4/15 11:48
# Author     ：bin
# version    ：python 3.7
"""

import pytest

from common.send_request import SendRequest

d = [
    "test_case/json_data/user/register.json",
    "test_case/json_data/user/login.json",
    "test_case/json_data/user/get_index.json",
    "test_case/json_data/user/shop_cart.json",
    "test_case/json_data/user/goods_detail.json"
]

@pytest.mark.auto
@pytest.mark.parametrize('file_path', d)
# 注册
def test_register(file_path):  # 同一个模块中方法名不能重复
    # 发送请求前的准备动作关键字列表
    pre_process = [

    ]
    # 收到响应后的后置操作关键字列表
    post_process = [
    ]

    # 怎么复制，看下方
    SendRequest(file_path).send_request(post_process=post_process, pre_process=pre_process)

d = [
    "test_case/json_data/user/register.json",
    "test_case/json_data/user/login.json"
]

@pytest.mark.smoke
@pytest.mark.parametrize('file_path', d)
# 注册
def test_register(file_path):  # 同一个模块中方法名不能重复
    # 发送请求前的准备动作关键字列表
    pre_process = [

    ]
    # 收到响应后的后置操作关键字列表
    post_process = [
    ]

    # 怎么复制，看下方
    SendRequest(file_path).send_request(post_process=post_process, pre_process=pre_process)


