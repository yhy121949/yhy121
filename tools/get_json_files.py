# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : get_json_files.py
# Time       ：2021/4/16 9:48
# Author     ：xuepl
# version    ：python 3.7
"""
import json
import os

from tools import log


def get_files(file_path, file_list):
    """
    获取给定文件夹下所有的.json文件
    :param file_path: 文件夹路径
    :param file_list: 文件列表
    :return:
    """
    print(file_path)
    files = os.listdir(file_path)
    for f in files:
        file = os.path.join(file_path, f)
        if os.path.isfile(file) and file.endswith(".json"):
            file_name = get_file_key(file)
            file_list.append(file_name)
        elif os.path.isdir(file):
            get_files(file, file_list)
        else:
            pass


def get_all_json_file(file_path):
    """
    获取指定文件夹及其子文件夹下所有的.json文件
    :return:
    """
    from tools.config_parser import ParseConfig
    root_path = ParseConfig().get_root_path()
    file_path = os.path.join(root_path, file_path)
    file_list = []
    get_files(file_path, file_list)
    log.debug("全部测试文件：{}".format(json.dumps(file_list, ensure_ascii=False, indent=2)))
    return file_list


def get_file_key(file_path):
    file_path = file_path.replace("\\", "/")
    file_path_list = file_path.split("/")
    length = len(file_path_list)
    if length == 1:
        return file_path_list[0]
    if "json_data" not in file_path:
        assert False, "json文件，必须存放于test_case/json_data文件夹及其子文件夹中"
    for i in range(length):
        if file_path_list[i] == "json_data":
            if length - 1 > i:
                file_path_list = file_path_list[i + 1:]
            break
    return "/".join(file_path_list)
