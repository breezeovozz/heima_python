class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果⼦配⽅]'
    def make_cake(self):
         print(f'运⽤{self.kongfu}制作煎饼果⼦')


class School(object):
     def __init__(self):
        self.kongfu = '[⿊⻢煎饼果⼦配⽅]'
     def make_cake(self):
        print(f'运⽤{self.kongfu}制作煎饼果⼦')
# 独创配⽅

class Prentice(School, Master):
    def __init__(self):
        self.kongfu = '[独创煎饼果⼦配⽅]'
    def make_cake(self):
        print(f'运⽤{self.kongfu}制作煎饼果⼦')
    def jsr(self):
        print('jsr1')
class ppp(Prentice):

    def jsr(self):
        print('jsr2')
    def fisrtjsr(self):
        Prentice.jsr(self)

# Prentice.jsr()


ppp().jsr()
ppp.jsr(ppp())
ppp.jsr(ppp)
# a.fisrtjsr()


#
# daqiu = Prentice()
# print(daqiu.kongfu)
# daqiu.make_cake()
