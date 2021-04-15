# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : data_acess.py
# Time       ：2021/4/10 9:31
# Author     ：xuepl
# version    ：python 3.7
"""
import json
import random
import re

from common import key_parser
import jsonpath

from tools import log


def set_var(send_request, var_name, var_value):
    """
    设置变量的值
    :param send_request: SendRequest对象实例
    :param var_name: 变量名
    :param var_value: 变量值，可包含关键字
    :return:
    """

    var_value = key_parser.Parser(var_value).keys_replace(send_request)
    send_request.local_var[var_name] = var_value


def get_var(send_request, var_name):
    """
    获取变量值
    :param send_request: SendRequest对象实例
    :param var_name: 变量名
    :return:
    """
    index = var_name.find("[")
    path = None
    name = var_name
    if index != -1:
        path = var_name[index:]
        name = var_name[:index]
    local_var = send_request.local_var
    value = None
    if name in local_var:
        value = local_var[name]
        if path:
            path = path.replace("'", "")
            path = path.replace('"', "")
            r = re.compile("\[(.*?)\]")
            res = r.findall(path)
            for k in res:
                value = value[k if not k.isdigit() else int(k)]
    log.debug("变量：{}的值为：{}".format(var_name, value))
    return value


def json_extractor(send_request, var_name, json_path, match_no="0", default=None):
    """
    根据jsonpath提取响应中的数据
    :param send_request: SendRequest对象实例
    :param var_name: 变量名
    :param json_path: jsonpath
    :param match_no: 匹配结果中的第几个，0表示随机取一个
    :param default: 默认值
    :return:
    """

    local_var = send_request.local_var
    data = json.loads(send_request.response.body)
    if len(data) == 0:
        if default:
            local_var[var_name] = default
        return
    json_path = json_path.replace("'", '"')
    json_path = json_path.replace('["', '.')
    json_path = json_path.replace('"]', '')
    res = jsonpath.jsonpath(data, json_path)
    print(res)
    if res:
        res = res[int(match_no) - 1] if match_no != "0" else random.choice(res)
        log.debug("提取结果为：{}".format(res))
        local_var[var_name] = res
