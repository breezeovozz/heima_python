def case1():
    return 22


def case2():
    return 33


def case3():
    return 44

switch={
1: case1,
2: case2,
3: case3
}


print(switch[3]())
print(case3)
