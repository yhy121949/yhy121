# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : common_data.py
# Time       ：2021/4/11 9:00
# Author     ：xuepl
# version    ：python 3.7
"""
import json

from tools import log


def replace_data(function):
    def func(*args, **kwargs):
        com_data = CommonData()
        send_request = args[0]
        if len(args) == 1 and "post_process" in kwargs and "pre_process" in kwargs:
            com_data.pre_process = kwargs["pre_process"]
            com_data.post_process = kwargs["post_process"]
        elif len(args) == 2 and "post_process" in kwargs:
            com_data.pre_process = args[1]
            com_data.post_process = kwargs["post_process"]
        elif len(args) == 3:
            com_data.pre_process = args[1]
            com_data.post_process = args[2]
        else:
            assert False, "send_request方法缺少必要参数"
        log.info("------------------执行前置步骤------------------")
        com_data.update_request(send_request)
        res = function(*args, **kwargs)
        log.info("-----------------执行后置操作-------------------")
        com_data.excute_post(send_request)
        return res

    return func


class CommonData():
    pre_process = None
    post_process = None

    @property
    def Parser(self):
        from common.key_parser import Parser
        return Parser

    def excute_post(self, send_request):
        """
        执行后置操作
        :return:
        """
        from tools import log
        if self.post_process:
            for s in self.post_process:
                log.debug(s)
                self.Parser(s).keys_replace(send_request)

    def update_request(self, send_request):
        """
        更新请求中的数据
        :param send_request:
        :return:
        """
        self.excute_pre(send_request)
        d = send_request.data
        d = self.Parser(d).keys_replace(send_request)
        send_request.data = json.loads(d)

    def update_dict(self, old, new):
        if isinstance(new, dict):
            for k in new:
                if k in old:
                    if isinstance(new[k], dict) or isinstance(new[k], list):
                        self.update_dict(old[k], new[k])
                    else:
                        old[k] = new[k]
        elif isinstance(new, list) and isinstance(old, list):
            length = len(new)
            for i in range(length):
                if isinstance(new[i], dict) or isinstance(new[i], list):
                    self.update_dict(old[i], new[i])
                else:
                    old[i] = new[i]
        else:
            pass

    def excute_pre(self, send_request):
        """
        执行前置操作
        :return:
        """
        if self.pre_process:
            for s in self.pre_process:
                log.debug(s)
                if isinstance(s, dict) or isinstance(s, list):
                    d = send_request.data
                    d = self.Parser(d).keys_replace(send_request)
                    d = json.loads(d)
                    self.update_dict(d, s)
                    print(d)
                    send_request.data = json.dumps(d, ensure_ascii=False, indent=2)
                else:
                    self.Parser(s).keys_replace(send_request)
