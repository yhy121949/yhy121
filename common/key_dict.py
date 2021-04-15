# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : key_dict.py
# Time       ：2021/4/2 9:06
# Author     ：xuepl
# version    ：python 3.7
"""
from tools.data_acess import set_var, get_var, json_extractor
from tools.make_datas import get_name, get_phone_number, get_full_address, get_detail_address, get_email, get_password, \
    get_text, get_color, get_credit_card_number, get_company, get_id_card, get_mac_address, get_ipv6, get_ipv4_public, \
    get_chrome, get_string, get_random_length_string, get_random_int
from tools.md5_tool import md5
from tools.mysql_tool import msyql_db
from tools.response_assert import assert_contains, assert_json

keys = dict(NAME=[get_name, "随机生成姓名 用法示例：$NAME()$"],
            PHONE=[get_phone_number, "随机生成手机号 用法示例：$PHONE()$"],
            FULL_ADDRESS=[get_full_address, "随机生成全量地址 用法示例：$FULL_ADDRESS()$"],
            STREET_ADDRESS=[get_detail_address, "随机生成街道地址 用法示例：$STREET_ADDRESS()$"],
            EMAIL=[get_email, "随机生成邮箱地址 用法示例：$EMAIL()$"],
            PASSWORD=[get_password, "随机生成密码 用法示例：$PASSWORD()$"],
            TEXT=[get_text, "随机生成一段文本 用法示例：$TEXT()$"],
            COLOR=[get_color, "随机生成颜色（英文） 用法示例：$COLOR()$"],
            CREDIT_CARD=[get_credit_card_number, "随机生成信用卡号 用法示例：$CREDIT_CARD()$"],
            COMPANY=[get_company, "随机生成公司名称 用法示例：$COMPANY()$"],
            ID_CARD=[get_id_card, "随机生成身份证号 用法示例：$ID_CARD()$"],
            MAC_ADDRESS=[get_mac_address, "随机生成mac地址 用法示例：$MAC_ADDRESS()$"],
            IPV6=[get_ipv6, "随机生成ipv6地址 用法示例：$IPV6()$"],
            IPV4=[get_ipv4_public, "随机生成ipv4地址 用法示例：$IPV64()$"],
            CHROME=[get_chrome, "随机生成chrome User-Agent 用法示例：$CHROME()$"],
            RANDOM_STRING=[get_string, "随机生成指定长度字符串 用法示例：$RANDOM_STRING(abcdefghijk,5)$ 结果示例：ceafk"],
            RANDOM_LENGTH_STRING=[get_random_length_string,
                                  "随机生成长度在指定范围内随机的字符串 用法示例：$RANDOM_LENGTH_STRING(abcdefghijk,5,20)$ 结果示例：ceafkjdi"],
            RANDOM_INT=[get_random_int, "随机生成整数 用法示例：$RANDOM_INT()$"],
            SET_VAR=[set_var, "设置变量的值 用法示例：$SET_VAR(var_name,var_value)$"],
            GET_VAR=[get_var, "获取变量的值 用法示例：$GET_VAR(var_name)$"],
            JSON_EXTRACTOR=[json_extractor, "json提取器，根据jsonpath提取响应正文中的数据 用法示例：$JSON_EXTRACTOR(var_name,json_path,0)$"],
            ASSERT_CONTAINS=[assert_contains, "断言响应正文中是否包含expect 用法示例：$ASSERT_CONTAINS(expect)$"],
            ASSERT_JSON=[assert_json, "断言响应json中json_path对应字段的值和expect的值是否相等 用法示例：$ASSERT_JSON(json_path,expect)$"],
            MYSQL=[msyql_db, "执行sql语句，并把执行结果存入变量var_name中 用法示例：$MYSQL(var_name,app,sql)$"],
            MD5=[md5, "md5加密 用法示例：$MD5(data)$"]
            )
