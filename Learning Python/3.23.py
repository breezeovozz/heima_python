class Digua(object):
    def __init__(self):
        self.status = '生的'
        self.roasttime = 0
        self.season = []

    def roast(self):
        time1 = int(input('请输入需要烤多少分钟'))
        self.roasttime += time1
        if self.roasttime <= 3:
            self.status = '地瓜现在是生的'
        elif 3 < self.roasttime <= 5:
            self.status = '地瓜现在半生不熟'
        elif 5 < self.roasttime <= 8:
            self.status = '地瓜现在是熟的'
        elif 8 < self.roasttime:
            self.status = '地瓜现在烤糊了'

    def Seasoning(self):
        season1 = input('请输入要添加的调料')
        self.season.append(season1)

    def __str__(self):
        str1 = ''
        for i in self.season:

            str1 += (i+' ')
        return (f'现在地瓜是{self.status},'
                f'现在地瓜上加了调料有这些：{str1}')

digua1 = Digua()
while 1:

    digua1.roast()
    digua1.Seasoning()
    print(digua1)
    flag = int(input('要退系统吗,是：输入0，否则不退出'))
    if not flag:
        break




