

def user_info(*args):
    print(args)
# ('TOM',)


user_info('TOM')
# ('TOM', 18)
user_info('TOM', 18)
    

def user_info(**kwargs):
    print(kwargs)


# {'name': 'TOM', 'age': 18, 'id': 110}
user_info(name='TOM', age=18, id=110)