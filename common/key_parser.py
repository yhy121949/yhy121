# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : key_parser.py
# Time       ：2021/4/2 9:42
# Author     ：xuepl
# version    ：python 3.7
"""

import re

from common.key_dict import keys


class Parser(object):

    def __init__(self, string):
        '''
        包含关键字的字符串
        :param string:
        '''
        self.string = string

    def get_key(self, string):
        """
        解析非嵌套关键字
        :param string:
        :return:
        """
        r = re.compile(r"\$(.*?)\$")
        return r.findall(string)

    def get_nesting_keys(self):
        """
        获取嵌套key
        :return:
        """
        string = self.string
        flag = 0
        start = 0
        keys = []
        ks = []
        length = len(string)
        for i in range(length):
            if string[i] == "$":
                if i == 0 or i == length - 1:
                    flag += 1
                elif string[i - 1] != ")" or string[i + 1].isupper():
                    flag += 1
                else:
                    pass
                if flag == 1:
                    start = i + 1
                if i > 0 and string[i - 1] == ")":
                    if flag == 2:
                        flag = 0
                        start = 0
                    if flag > 2 and flag % 2 == 0:
                        keys.append(string[start:i])
                        ks.append(string[start:i])
                        flag = 0
                        start = 0
        for k in ks:
            r = re.compile(r"\$(.*?)\$")
            res = r.findall(k)
            if len(res) != 0:
                keys.append(res)
        return keys, ks

    def get_single_key(self, s):
        """

        :param s:
        :return:
        """
        start = 0
        length = len(s)
        keys = []
        flag = False
        for i in range(length):
            if s[i] == '$':
                if not flag:
                    start = i + 1
                    flag = True
                else:
                    if s[i - 1] == ")":
                        keys.append(s[start:i])

        return keys

    @property
    def keys(self):
        """
        返回数据中的所有关键字的列表
        :return:
        """
        keys, ks = self.get_nesting_keys()
        s = self.string
        for k in ks:
            s = s.replace("$" + k + "$", "")
        res = self.get_single_key(s)
        if len(res) != 0:
            keys.append(res)
        return keys

    def get_func_name(self, key):
        """
        获取关键字中的方法名
        :param key:关键字
        :return:
        """
        r = re.compile(r"^(.*)\(")
        res = r.findall(key)
        if len(res) != 0 and res[0] != "":
            return keys[res[0].upper()]
        return None

    def get_args(self, key):
        """
        获取关键字中的参数列表
        :param key:关键字
        :return:
        """
        r = re.compile(r"\((.*)\)")
        res = r.findall(key)
        if len(res) != 0 and res[0] != "":
            return res[0].split(",")
        return None

    def excute_key(self, send_request, key):
        """
        :param send_request: SendRequest对象实例
        根据关键字运行对应的方法生成数据
        :param key:关键字
        :return:
        """
        func_name = self.get_func_name(key)
        args = self.get_args(key)
        if func_name:
            if args:
                return func_name[0](send_request, *args)
            return func_name[0](send_request)

    def replace_key_and_str(self, keys, key, res):
        """
        替换关键字列表中的嵌套关键字和数据
        :param keys: 关键字列表
        :param key: 被替换关键字
        :param res: 关键字执行结果
        :return:
        """
        if not res:
            return
        if not isinstance(res, str):
            res = str(res)
        length = len(keys)
        for i in range(length):
            if isinstance(keys[i], str) and key in keys[i]:
                key_1 = keys[i].replace("${}$".format(key), res, 1)
                self.string = self.string.replace("${}$".format(keys[i]), key_1, 1)
                keys[i] = key_1

    def replace_str(self, key, res):
        """
        关键字替换，替换所有数据中的关键字
        :param key: 被替换关键字
        :param res: 关键字运行结果
        :return:
        """
        if not res:
            return
        if not isinstance(res, str):
            res = str(res)
        self.string = self.string.replace("${}$".format(key), res, 1)

    def keys_replace(self, send_request):
        """
        根据keys列表，替换所有的数据
        :param send_request: SendRequest对象实例
        :return:
        """
        keys = self.keys
        length = len(keys)
        for i in range(length):
            if isinstance(keys[i], list):
                for k in keys[i]:
                    res = self.excute_key(send_request, k)
                    if i != length - 1:
                        self.replace_key_and_str(keys, k, res)
                    else:
                        self.replace_str(k, res)
        for k in keys:
            if isinstance(k, str):
                res = self.excute_key(send_request, k)
                self.replace_str(k, res)
        return self.string
