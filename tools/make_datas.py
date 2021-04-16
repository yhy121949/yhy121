# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : aaaa.py
# Time       ：2021/4/1 19:15
# Author     ：xuepl
# version    ：python 3.7
"""
import random

from faker import Faker

fake = Faker("zh_CN")  # 默认英文，初始化为中文


def get_name(send_request):
    """
    随机生成姓名
    :param send_request: SendRequest对象实例
    :return:
    """
    return fake.name()


def get_full_address(send_request):
    """
    随机生成全量地址
    :param send_request: SendRequest对象实例
    :return:
    """

    return fake.address()


def get_detail_address(send_request):
    """
    随机生成详细地址
    :param send_request: SendRequest对象实例
    :return:
    """

    return fake.street_address()


def get_email(send_request):
    """
    随机生成邮箱
    :param send_request: SendRequest对象实例
    :return:
    """
    return fake.email()


def get_password(send_request):
    """
    随机生成密码
    :param send_request: SendRequest对象实例
    :return:
    """
    return fake.password()


def get_text(send_request):
    """
    随机生成一大段文本
    :param send_request: SendRequest对象实例
    :return:
    """
    return fake.text()


def get_color(send_request):
    """
    随机生成颜色（英文表示）
    :param send_request: SendRequest对象实例
    :return:
    """
    return fake.color_name()


def get_credit_card_number(send_request):
    """
    随机生成信用卡卡号
    :param send_request: SendRequest对象实例
    :return:
    """
    while True:
        card_number = fake.credit_card_number(card_type=None)
        if card_number.startswith("6"):
            return card_number


def get_company(send_request):
    """
    随机生成公司名称
    :param send_request: SendRequest对象实例
    :return:
    """
    return fake.company()


def get_phone_number(send_request):
    """
    随机生成手机号
    :param send_request: SendRequest对象实例
    :return:
    """
    return fake.phone_number()


def get_id_card(send_request):
    """
    随机生成身份证
    :param send_request: SendRequest对象实例
    :return:
    """
    return fake.ssn(min_age=18, max_age=90)


def get_mac_address(send_request):
    """
    随机生成mac地址
    :param send_request: SendRequest对象实例
    :return:
    """
    return fake.mac_address()


def get_ipv6(send_request):
    """
    随机生成ipv6地址
    :param send_request: SendRequest对象实例
    :return:
    """
    return fake.ipv6(network=False)


def get_ipv4_public(send_request):
    """
    随机生成ipv4地址
    :param send_request: SendRequest对象实例
    :return:
    """
    return fake.ipv4(network=False, address_class=None, private=None)


def get_chrome(send_request):
    """
    伪造chrome浏览器
    :param send_request: SendRequest对象实例
    :return:
    """
    return fake.chrome(version_from=13, version_to=63, build_from=800, build_to=899)


def get_random_length_string(send_request, content, start, end):
    """
    随机生成指，长度在start到end之间，字符在content之中选择的字符串
    :param send_request: SendRequest对象实例
    :param content: 字符选择范围，字符串
    :param start: 最小长度 整数
    :param end: 最大长度 整数
    :return:
    """
    if not isinstance(start, int):
        start = int(start.strip())
    if not isinstance(end, int):
        start = int(end.strip())
    length = random.randint(start, end)
    return "".join(random.choices(content, k=length))


def get_string(send_request, content, length):
    """
    随机生成指，长度为length，字符在content之中选择的字符串
    :param send_request: SendRequest对象实例
    :param content:
    :param length:
    :return:
    """
    if not isinstance(length, int):
        length = int(length.strip())
    return "".join(random.choices(content, k=length))


def get_random_int(send_request, start, end):
    """
    随机生成min至max之间的整数
    :param send_request: SendRequest对象实例
    :param start: 最小值
    :param end: 最大值
    :return:
    """
    if not isinstance(start, int):
        start = int(start.strip())
    if not isinstance(end, int):
        start = int(end.strip())
    return random.randint(start, end)


if __name__ == '__main__':
    # print(get_name())
    print(get_full_address())
    # print(get_email())
    # print(get_password())
    # print(get_text())
    # print(get_color())
    # print(get_credit_card_number())
    print(get_detail_address())
    print(get_company())
    print(get_random_length_string("123456789", 3, 6))
