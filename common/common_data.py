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
        pre_process = json.loads(com_data.get_json_pre_or_post(send_request, "pre_process"))
        post_process = json.loads(com_data.get_json_pre_or_post(send_request, "post_process"))
        post_process.extend(com_data.post_process if isinstance(com_data.post_process, list) else [])
        pre_process.extend(com_data.pre_process if isinstance(com_data.pre_process, list) else [])
        com_data.post_process = post_process
        com_data.pre_process = pre_process
        log.info("------------------执行前置步骤------------------")
        com_data.update_request(send_request)
        res = function(*args, **kwargs)
        log.info("-----------------执行后置操作-------------------")
        com_data.excute_post(send_request)
        log.debug("全部变量：{}".format(send_request.local_var))
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

        data = send_request.data
        if isinstance(self.post_process, list):
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
        send_request.data = d

    def update_dict(self, old, new):
        """
        新字典中的数据替换旧字典
        :param old: 旧字典
        :param new: 新字典
        :return:
        """
        if isinstance(new, dict) and isinstance(old, dict):
            for k in new:
                if k in old:
                    if (isinstance(new[k], dict) and isinstance(old[k], dict)) or (
                            isinstance(new[k], list) and isinstance(old[k], list)):
                        self.update_dict(old[k], new[k])
                    else:
                        old[k] = new[k]
        elif isinstance(new, list) and isinstance(old, list):
            length = len(new)
            for i in range(length):
                if i < len(old):
                    if (isinstance(new[i], dict) and isinstance(old[i], dict)) or (
                            isinstance(new[i], list) and isinstance(old[i], list)):
                        self.update_dict(old[i], new[i])
                    else:
                        old[i] = new[i]
                else:
                    old.append(new[i])
        else:

            pass

    def get_json_pre_or_post(self, send_request, key):
        """
        字符串解析的形式，获取json文件中pre_process或者post_process的值
        :param send_request:
        :param key: "pre_process" or "post_process"
        :return:
        """
        data = send_request.data
        if key not in ["pre_process", "post_process"]:
            return '[]'
        index = data.find(key)
        if index == -1:
            return '[]'
        data = data[index:]
        data = data[data.find(":") + 1:]
        start = 0
        flag = False
        k = 0
        for i in range(len(data)):
            if k == 0 and data[i] == ",":
                return '[]'
            if data[i] == "[":
                if k == 0:
                    flag = True
                    start = i
                k -= 1
            elif data[i] == ']':
                k += 1
            else:
                pass
            if flag and k == 0:
                data = data[start:i + 1]
                send_request.data = send_request.data.replace(data, "[]")
                return data
        return '[]'

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
                    send_request.data = json.dumps(d, ensure_ascii=False, indent=2)
                else:
                    self.Parser(s).keys_replace(send_request)
