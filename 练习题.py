# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 练习题.py
# Time       ：2021/4/18 10:15
# Author     ：yhy
# version    ：python 3.7
"""
l = [1, 3, 45, 39, 9, 66]
def test1(list, n):
    print(list)
    for i in range(n):
        list.insert(0, list.pop())
        print(list)

def test2(list, n):
    print(list)
    for i in range(n):
        num=list[len(list)-1]
        list.remove(num)
        list.insert(0, num)
        print(list)


test1([1, 3, 45, 39, 9, 66], 2)
print("-------------")
test2([1, 3, 45, 39, 9, 66], 2)
