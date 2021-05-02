#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2021/3/26 19:51
# @Author  : Asus
# @File    : 3.26.3.py
# @Software: PyCharm
"""

"""
文件说明：
"""
class Dog(object):
    @staticmethod
    def infoprint():
        print('这是静态方法')


A = Dog()
A.infoprint()
Dog.infoprint()
print(1)