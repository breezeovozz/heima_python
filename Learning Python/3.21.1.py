# """
# 列表推导式
# """
#
# list1 = []
# list2 = []
#
# def fun():
#     i = 0
#     while i < 11:
#         list1.append(i)
#         i += 1
#
#
# fun()
# print(list1)
#
#
# def for_list2():
#     for i in range(11):
#         list2.append(i)
#
#
# for_list2()
# print(list2)
#
# list3 = [(i+1) for i in range(10)]
# print(list3)
#
# list4 = [i for i in range(0, 11, 2)]
# print(list4)
#
# list5 = [i for i in range(11) if i % 2 == 0]
# print(list5)
#
# list6 = []
# for i in range(1,3):
#     for j in range(3):
#         list6.append((i,j))
#
#
# print(list6)
#
# list7 = [(i, j) for i in range(1,3) for j in range(3)]
#
# print(list7)
#

"""
创建字典 key是1-5，value是1-5的平方

"""

dict1 = {i: i**2 for i in range(1, 6)}

print(dict1)

list1 = ['aw', '22', '33']
list2 = ['asd', 'dadw', '112', 'dad']

for i in range(len(list1)):
    dict1[list1[i]] = list2[i]
print(dict1)

print(max(len(list2),len(list1)))

list1 = [('jsr', 88), ('wcc', 89), ('wjs', 100), ('wsr', 98)]

list2 = [['jsr', 88], ['wcc', 89], ['wjs', 100], ['wsr', 98]]

newlist1 = []
newlist2 = []
for name, grade in list1:
    if grade > 90:
        newlist1.append((name, grade))

for name, grade in list2:
    if grade > 90:
        newlist2.append([name, grade])


print(f'第一种{newlist1},\n第二种{newlist2}')

