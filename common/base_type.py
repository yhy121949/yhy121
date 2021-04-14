# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : base_type.py
# Time       ：2021/4/8 8:20
# Author     ：xuepl
# version    ：python 3.7
"""


class Singleton(type):
    # def __init__(self, *args, **kwargs):
    #     self.__instance = None
    #     super(Singleton, self).__init__(*args, **kwargs)
    __instance = None

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super(Singleton, self).__call__(*args, **kwargs)
        return self.__instance
