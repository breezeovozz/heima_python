# """
# 打印正方形的星号
# """
# for i in range(5):
#     for j in range(5):
#         print('*', end='')
#
#     print()
#
# print('------打印正方形结束-----')
# """
# 打印三角形的星号
# """
#
# m = 0
# n = 5
# for j in range(n):
#     m = j+1
#     for i in range(m):
#
#         print('*', end='')
#     for h in range(5 - m):
#         print('&', end='')
#     print()
# print('----打印三角形结束----')

print('九九乘法表')

i = 0
while i < 9:
    j = 0
    while j <= i:
        print(f'{j+1} * {i+1} = {(j+1)*(i+1)}', end='\t')
        j += 1
    print()
    i += 1
