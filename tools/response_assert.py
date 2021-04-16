# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : response_assert.py
# Time       ：2021/4/10 11:17
# Author     ：xuepl
# version    ：python 3.7
"""
import json

import allure
import jsonpath


def assert_contains(send_request, expect):
    """
    断言响应正文中是否包含expect
    :param send_request: SendRequest对象实例
    :param expect: 预期结果
    :return:
    """
    from common.key_parser import Parser
    if not hasattr(send_request, "response"):
        return
    expect = Parser(expect).keys_replace(send_request)
    body = send_request.response.body
    allure.attach("预期结果：{}\n响应正文：{}".format(expect, body), "----------响应正文断言，包含--------------",
                  allure.attachment_type.TEXT)
    assert expect in body, "预期结果：{}\n响应正文：{}".format(expect, body)


def assert_json(send_request, json_path, expect):
    """
    断言响应json中json_path对应字段的值和expect的值是否相等
    :param send_request: SendRequest对象实例
    :param json_path: json_path
    :param expect: 预期结果
    :return:
    """
    from common.key_parser import Parser
    if not hasattr(send_request, "response"):
        return
    expect = Parser(expect).keys_replace(send_request)
    data = json.loads(send_request.response.body)
    json_path = json_path.replace("'", '"')
    json_path = json_path.replace('["', '.')
    json_path = json_path.replace('"]', '')
    res = jsonpath.jsonpath(data, json_path)
    allure.attach("预期结果：{}\n 实际结果：{}".format(
        expect, res), "----------json断言，等于--------------", allure.attachment_type.TEXT)
    if res:
        assert res[0] == expect if isinstance(res[0], str) else str(res[0]) == expect, "预期结果：{}\n 实际结果：{}".format(
            expect, res[0])
    else:
        assert False, "json_path：{}在响应正文：{}中无法匹配出结果".format(json_path, data)
