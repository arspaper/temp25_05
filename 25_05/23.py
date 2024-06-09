def func(x, y):
    if x == y:
        return 1
    if x > y:
        return 0
    else:
        return func(x + 1, y) + func(x + 2, y) + func(x * 2, y)
    
print(func(4, 11) * func(11, 13) * func(13, 15))