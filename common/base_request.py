# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : base_request.py
# Time       ：2021/4/2 8:45
# Author     ：xuepl
# version    ：python 3.7
"""
import json
import os

import allure

from tools import log
from tools.config_parser import ParseConfig


class BaseRequest():

    def __init__(self, d):
        self.__headers = {"User-Agent": self.Parser("$CHROME()$").keys_replace(None)}
        config = ParseConfig()
        if isinstance(d, str):
            d = json.loads(d)
        self.__base_url = config.get_url(d.get("service"))
        self.__uri = d.get("url")
        self.__headers.update(d.get("headers", {}))
        self.__body = d.get("body")
        self.__method = d.get("method")
        self.__files = d.get("files")
        for k in d:
            if k in ['feature', 'story', 'title']:
                getattr(allure.dynamic, k)(d[k])

    @property
    def Parser(self):
        from common.key_parser import Parser
        return Parser

    @property
    def url(self):
        if not self.__uri:
            log.error("url不能为空")
            assert False, "url不能为空"
        if not self.__uri.startswith("/"):
            self.__uri = "/" + self.__uri

        return self.__base_url + self.__uri

    @property
    def method(self):
        if not self.__method or self.__method == "":
            self.__method = "GET"
        return self.__method.upper()

    @property
    def headers(self):
        if not self.__body:
            return self.__headers
        if "Content-Type" not in self.__headers or "content-type" not in self.__headers:
            if isinstance(self.__body, dict):
                self.__headers["Content-Type"] = "application/json"
            elif isinstance(self.__body, str) and "=" in self.__body:
                self.__headers["Content-Type"] = "application/x-www-form-urlencoded"
            else:
                pass
        return self.__headers

    @property
    def body(self):
        if isinstance(self.__body, dict):
            return json.dumps(self.__body, ensure_ascii=False, indent=2)
        return self.__body

    @property
    def files(self):
        if not self.__files:
            return None
        if isinstance(self.__files, dict):
            root_path = ParseConfig().get_root_path()
            for k, v in self.__files.items():
                file_path = os.path.join(root_path, v)
                if os.path.isfile(file_path):
                    self.__files[k] = open(file_path, 'rb')
                else:
                    log.error("文件：{}不存在".format(file_path))
                    assert False, "文件：{}不存在".format(file_path)
        else:
            log.error('files字段需要字典格式，示例：{"file":"test_case\\data\\name.xls"}')
            assert False, 'files字段需要字典格式，示例：{"file":"test_case\\data\\name.xls"}'
        return self.__files
