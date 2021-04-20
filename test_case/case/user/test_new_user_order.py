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


def test_login():
    # 发送请求前的准备动作
    pre_process = [
        {"body": {
            "loginName": "$GET_VAR(phone)$"
        }}
    ]
    # 收到响应后的后置操作
    post_process = [
        "$JSON_EXTRACTOR(token,$.data,0)$"
    ]
    print(SendRequest("test_case/json_data/user/login.json").send_request(post_process=post_process,
                                                                          pre_process=pre_process).local_var)


def test_get_index():
    # 发送请求前的准备动作
    pre_process = [
    ]
    # 收到响应后的后置操作
    post_process = [
        "$JSON_EXTRACTOR(goodsId,$['data']['hotGoodses'][*]['goodsId'],2)$"
    ]
    print(SendRequest("test_case/json_data/user/get_index.json").send_request(post_process=post_process,
                                                                              pre_process=pre_process).local_var)


def test_shop_cart():
    # 发送请求前的准备动作
    pre_process = [
    ]
    # 收到响应后的后置操作
    post_process = [
    ]
    print(SendRequest("test_case/json_data/user/shop_cart.json").send_request(post_process=post_process,
                                                                              pre_process=pre_process).local_var)


def test_new_address():
    # 发送请求前的准备动作
    pre_process = [
    ]
    # 收到响应后的后置操作
    post_process = [
    ]
    print(SendRequest("test_case/json_data/user/new_address.json").send_request(post_process=post_process,
                                                                                pre_process=pre_process).local_var)


def test_address():
    # 发送请求前的准备动作
    pre_process = [
    ]
    # 收到响应后的后置操作
    post_process = [
        "$JSON_EXTRACTOR(addressId,$['data'][0]['addressId'])$"
    ]
    print(SendRequest("test_case/json_data/user/address.json").send_request(post_process=post_process,
                                                                            pre_process=pre_process).local_var)


def test_cart():
    # 发送请求前的准备动作
    pre_process = [
    ]
    # 收到响应后的后置操作
    post_process = [
        "$JSON_EXTRACTOR(cartItemId,$['data']['list'][0]['cartItemId'])$"
    ]
    print(SendRequest("test_case/json_data/user/cart.json").send_request(post_process=post_process,
                                                                         pre_process=pre_process).local_var)


def test_saveOrder():
    # 发送请求前的准备动作
    pre_process = [
    ]
    # 收到响应后的后置操作
    post_process = [
        "$JSON_EXTRACTOR(orderNo,$['data'])$"
    ]
    print(SendRequest("test_case/json_data/user/saveOrder.json").send_request(post_process=post_process,
                                                                              pre_process=pre_process).local_var)


def test_paySuccess():
    # 发送请求前的准备动作
    pre_process = [
    ]
    # 收到响应后的后置操作
    post_process = [
    ]
    print(SendRequest("test_case/json_data/user/paySuccess.json").send_request(post_process=post_process,
                                                                               pre_process=pre_process).local_var)
