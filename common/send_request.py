# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : send_request.py
# Time       ：2021/4/2 8:46
# Author     ：xuepl
# version    ：python 3.7
"""
import json
import os

import allure
import requests

from common.base_request import BaseRequest
from common.base_response import BaseResponse
from common.common_data import replace_data
from tools import log


class SendRequest():
    json_data_files = {}
    session = requests.Session()
    local_var = {}

    def __init__(self, json_file):
        if len(self.json_data_files) == 0:
            self.get_all_json_file()
        json_file = json_file.replace("\\", "/")
        json_file = self.get_file_key(json_file)
        # log.debug(json_file)
        if json_file not in self.json_data_files:
            log.error("json文件：{} 不存在".format(json_file))
            assert False, "json文件：{} 不存在".format(json_file)
        self.data = self.read_file(self.json_data_files[json_file])

    def clear(self):
        self.request = None
        self.response = None

    @property
    def config(self):
        from tools.config_parser import ParseConfig
        return ParseConfig()

    @replace_data
    def send_request(self, pre_process, post_process):
        """
        主方法，发送请求
        :param pre_process: 请求前的操作
        :param post_process: 收到响应后的操作
        :return:
        """
        self.clear()
        self.request = BaseRequest(self.data)
        log.info("--------------获取请求数据-------------------")
        requst_data = self.__get_request_data()
        log.info("--------------发送请求----------------------")
        if "data" in requst_data:
            requst_data["data"] = requst_data["data"].encode("utf-8") if requst_data["data"] else None
        response = self.__send_request(requst_data)
        log.debug("响应状态码为：{}".format(response.status_code))
        self.response = BaseResponse(response)
        log.info("--------------获取响应数据----------------------")
        self.__get_response_data()
        return self

    def __format_headers(self, headers):
        """
        把字典数据转化成请求头的格式
        :param headers: 请求头字典
        :return:
        """
        headers_list = ["{}: {}".format(k, v) for k, v in headers.items()]
        return "\n".join(headers_list)

    def __get_request_data(self):
        """
        获取请求数据，并打印请求信息日志
        :return:
        """
        body = None if not self.request.body or len(self.request.body) == 0 else self.request.body
        method = self.request.method
        url = self.request.url
        headers = self.request.headers
        files = None if not self.request.files or len(self.request.files) == 0 else self.request.files

        request_data = """{} {}
{}

{}""".format(method, url, self.__format_headers(headers), body if body else "" if not files else "文件内容")
        log.debug(request_data)
        allure.attach(request_data, "--------------------请求数据--------------------", allure.attachment_type.TEXT)
        return {"data": body, "method": method, "url": url, "headers": headers, "files": files}

    def __send_request(self, data):
        return self.session.request(**data)

    def __get_response_data(self):
        """
        获取响应数据，并打印响应信息日志
        :return:
        """
        status_code = self.response.status_code
        headers = self.response.headers
        body = self.response.body
        response_data = """{}
{}

{}
        """.format(status_code, self.__format_headers(headers), body if body else "")
        log.debug(response_data)
        allure.attach(response_data, "--------------------响应数据--------------------", allure.attachment_type.TEXT)

    def read_file(self, file_path):
        """
        读取文件全部内容
        :param file_path:文件路径
        :return:
        """
        with open(file_path, encoding="utf-8") as f:
            return f.read()

    def get_all_json_file(self):
        """
        获取test_case\\json_data文件夹及其子文件夹下所有的.json文件
        :return:
        """
        if len(self.json_data_files) == 0:
            json_data_dir = self.config.get_json_data()
            self.get_files(json_data_dir)
        log.debug("全部文件路径为：{}".format(json.dumps(self.json_data_files, ensure_ascii=False, indent=2)))

    def get_file_key(self, file_path):
        file_path = file_path.replace("\\", "/")
        file_path_list = file_path.split("/")
        length = len(file_path_list)
        if length == 1:
            return file_path_list[0]
        if "json_data" not in file_path:
            return "/".join(file_path_list)
        for i in range(length):
            if file_path_list[i] == "json_data":
                if length - 1 > i:
                    file_path_list = file_path_list[i + 1:]
                break
        return "/".join(file_path_list)

    def get_files(self, file_path):
        """
        获取给定文件夹下所有的.json文件
        :param file_path: 文件夹路径
        :return:
        """
        files = os.listdir(file_path)

        for f in files:
            file = os.path.join(file_path, f)
            if os.path.isfile(file) and file.endswith(".json"):
                file_name = self.get_file_key(file)
                self.json_data_files[file_name] = file
            elif os.path.isdir(file):
                self.get_files(file)
            else:
                pass
