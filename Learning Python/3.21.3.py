
student1 = []
while 1:

    def add_student():
        """
        这是添加学员函数
        :return:
        """
        student = input('请输入要添加的学员名字')
        student1.append(student)


    def del_student():
        student = input('请输入要删除的学员名字')
        student1.remove(student)


    def print_student():
        print(student1)


    def get_unk():
        return 'unknow'

    print('--------这里是学员管理系统--------')
    print('1、 添加学员')
    print('2、 删除学员')
    print('3、 修改学员信息')
    print('4、 查询学员信息')
    print('5、 显示所有学员信息')
    print('6、 退出系统')
    print('--------这里是学员管理系统--------')
    fun = {
        1: add_student,
        2: del_student,
        5: print_student

    }

    fun_num = int(input('请输入功能所对应的序号'))
    if fun_num == 6:
        break
    else:
        fun.get(fun_num, get_unk())()






