from student import *
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2021/4/3 21:58
# @Author  : Asus
# @File    : managerSystem.py
# @Software: PyCharm
"""

"""
文件说明：管理系统
"""



class StudentManager(object):
    def __init__(self):
        self.student_list = []

    # 程序入口函数
    def run(self):
        # 加载学员数据
        self.load_student()
        while 1:
            # 显示功能菜单
            self.show_menu()
            # 用户输入目标功能序号
            menu_num = int(input('请输入要执行的操作：'))
            # 根据输入的序号执行不同的功能
            if menu_num == 1:
                self.add_student()
            elif menu_num == 2:
                self.del_student()
            elif menu_num == 3:
                self.modify_student()
            elif menu_num == 4:
                self.search_student()
            elif menu_num == 5:
                self.print_student()
            elif menu_num == 6:
                self.save_student()
            elif menu_num == 7:
                break

    @staticmethod
    def show_menu():
        print('--------请选择如下功能-----------------')
        print('1:添加学员')
        print('2:删除学员')
        print('3:修改学员信息')
        print('4:查询学员信息')
        print('5:显示所有学员信息')
        print('6:保存学员信息')
        print('7:退出系统')

    def add_student(self):
        name = input('请输入学生的姓名：')
        sex = input('请输入学生的性别：')
        tel = input('请输入学生的电话号码：')
        stu = Student(name, sex, tel)
        self.student_list.append(stu)
        print(self.student_list)

    def del_student(self):
        del_name = input('请输入要删除的学员名字：')
        for stu_object in self.student_list:
            if stu_object.name == del_name:
                self.student_list.remove(stu_object)
                break
        else:
            print('查无此人,请输入其他姓名')
        print(self.student_list)

    def modify_student(self):
        modify_name = input('请输入要修改的学员名字：')
        for stu_object in self.student_list:
            if stu_object.name == modify_name:
                stu_object.name = input('请输入新的名字：')
                stu_object.phone_number = input('请输入新的电话号码：')
                stu_object.sex = input('请输入新的性别：')
                print(f'信息修改成功，姓名{stu_object.name},'
                      f'号码{stu_object.phone_number},性别{stu_object.sex}')
                break
        else:
            print('没有这个人请输入其他姓名修改')

    def search_student(self):
        search_name = input('请输入要查询的学员名字：')
        for stu_object in self.student_list:
            if stu_object.name == search_name:
                print(f'姓名{stu_object.name},'
                      f'号码{stu_object.phone_number},性别{stu_object.sex}')
                break
        else:
            print('查无此人,请输入其他姓名')

    def print_student(self):
        print('姓名\t性别\t⼿机号')
        for i in self.student_list:
            print(f'{i.name}\t{i.sex}\t{i.phone_number}')

    def save_student(self):
        f = open('student.data', 'w')
        new_list = []
        for stu_object in self.student_list:
            new_list.append(stu_object.__dict__)
        # new_list = [i.__dict__ for i in self.student_list] 可以用这行代替上面的3行
        f.write(str(new_list))
        f.close()

    def load_student(self):
        try:
            f = open('student.data', 'r')
        except:
            f = open('student.data', 'w')
        else:
            data = f.read()
            new_list = eval(data)
            # self.student_list = []
            # for i in new_list:
            #     self.student_list.append(Student(i['name'], i['sex'],i['phone_number']))
            self.student_list = [Student(i['name'], i['sex'],i['phone_number'])
                                 for i in new_list]
        finally:
            f.close()
