#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2021/4/3 21:58
# @Author  : Asus
# @File    : student.py
# @Software: PyCharm
"""

"""
文件说明：学生角色代码
"""


class Student(object):
    def __init__(self, name, sex, phone_number):
        self.name = name
        self.sex = sex
        self.phone_number = phone_number

    def __str__(self):
        return f'{self.name}, {self.sex}， {self.phone_number}'


