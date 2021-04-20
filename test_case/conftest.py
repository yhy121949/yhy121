# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : conftest.py
# Time       ：2021/4/15 11:22
# Author     ：xuepl
# version    ：python 3.7
"""
def pytest_collection_modifyitems(session, config, items) -> None:
    # item表示每个测试用例，解决用例名称中文显示问题
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode-escape")
        item._nodeid = item._nodeid.encode("utf-8").decode("unicode-escape")