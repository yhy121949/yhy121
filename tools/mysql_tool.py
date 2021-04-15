# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : mysql_tool.py
# Time       ：2021/4/15 8:06
# Author     ：xuepl
# version    ：python 3.7
"""
import contextlib

import pymysql

from tools.config_parser import ParseConfig


class PyMySQL():
    def __init__(self, host, user, password, database, port=3306, charset="utf8"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.charset = charset

    @contextlib.contextmanager
    def connect(self):
        """
        连接数据库
        :return:
        """
        con = pymysql.connect(host=self.host,
                              user=self.user,
                              password=self.password,
                              database=self.database,
                              port=self.port,
                              charset=self.charset,
                              cursorclass=pymysql.cursors.DictCursor)
        cursor = con.cursor()
        try:
            yield cursor
        except Exception as e:
            print(e)
            print("sql执行失败")
        finally:
            con.commit()
            cursor.close()
            con.close()

    def query(self, sql):
        with self.connect() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()


def msyql_db(send_request, var_name=None, app="", sql=""):
    """
    执行sql语句，并把执行结果存入变量var_name中
    :param send_request:
    :param var_name: 变量名
    :param app: 子系统名称
    :param sql: sql语句
    :return:
    """
    db = PyMySQL(**send_request.config.get_db_config(app))
    if app == "" or sql == "":
        return
    send_request.local_var[var_name] = db.query(sql)


if __name__ == '__main__':
    db = PyMySQL("mysql.xuepl.com.cn", "root", "Xue00011133", "pms", port=3306)
