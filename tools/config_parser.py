# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : config_parser.py
# Time       ：2021/4/1 18:54
# Author     ：xuepl
# version    ：python 3.7
"""

import configparser
import os

from tools import log

root_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
config = configparser.ConfigParser()
config_path = os.path.join(root_path, "config.ini")
config.read(config_path, encoding="utf-8")


class ParseConfig():

    def __init__(self):
        self.env = self.get_config("env", "env")

    def __get_sections(self):
        """
        获取config.ini中的所有sections
        :return:
        """
        return config.sections()

    def __get_options(self, section):
        """
        获取congfig.ini文件中，对应section下的所有options
        :param section: section
        :return:
        """
        return config.options(section)

    def __get_items(self, section):
        """
        获取section下所有配置信息
        :param section: section
        :return:
        """
        return {c[0]: c[1] for c in config.items(section)}

    def get_url(self, app):
        """
        获取应用url
        :param app: config.ini文件中应用名
        :return:
        """
        url = self.get_config(self.env + "_url", app)
        if url.startswith("http://") or url.startswith("https://"):
            pass
        else:
            url = "http://" + url
        if url.endswith("/"):
            return url[:-1]
        return url

    def get_db_config(self, app):
        """
        获取应用数据库连接配置信息
        :param app: config.ini文件中应用名
        :return:
        """
        app = "{}_{}_db".format(self.env, app)
        if app not in self.__get_sections():
            log.error("db配置：{} 在config.ini文件中不存在".format(app))
            return None
        return self.__get_items(app)

    def get_config(self, section, option):
        if section not in self.__get_sections():
            log.error("section：{} 在config.ini文件中不存在".format(section))
            return None
        if option not in self.__get_options(section):
            log.error("option：{}在config.ini文件的section：{}中不存在".format(option, section))
            return None

        return config.get(section, option)

    def get_root_path(self):
        self.root_path = self.get_config("base", "root_path")
        if self.root_path == "":
            return root_path
        return self.root_path

    def get_json_data(self):
        return os.path.join(self.get_root_path(), 'test_case\json_data')


if __name__ == '__main__':
    print(ParseConfig().get_json_data())
