# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : base_response.py
# Time       ：2021/4/8 20:40
# Author     ：xuepl
# version    ：python 3.7
"""
import json


class BaseResponse():

    def __init__(self, response):
        self.__response = response



    @property
    def status_code(self):
        return self.response.status_code

    @property
    def headers(self):
        return self.response.headers

    @property
    def body(self):
        if self.response.json() and len(self.response.json()) != 0:
            return json.dumps(self.response.json(), ensure_ascii=False, indent=2)
        return self.response.text

    @property
    def response(self):
        return self.__response
