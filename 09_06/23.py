def func(x, y):
    if x == y:
        return 1
    if x > y or x == 18:
        return 0
    else:
        return func(x + 1, y) + func(x * 2, y)
    
print(func(1, 10) * func(10, 21))