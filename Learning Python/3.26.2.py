#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2021/3/26 15:15
# @Author  : Asus
# @File    : 3.26.2.py
# @Software: PyCharm
"""

"""
文件说明：多态0
"""


class Dog(object):
    def work(self):
        print('指哪打哪。。')


class ArmyDog(Dog):
    def work(self):
        print('追击敌人')


class DrugDog(Dog):
    def work(self):
        print('追查毒品')


class Person(object):
    def work_with_dog(self, dog):
        dog.work()
    def work(self):
        print('人跑路')
armydog = ArmyDog()
drugdog = DrugDog()
tiancai = Person()

tiancai.work_with_dog(drugdog)
tiancai.work_with_dog(tiancai)




