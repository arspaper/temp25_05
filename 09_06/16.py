from sys import setrecursionlimit

setrecursionlimit(100000)


def func(n):
    if n >= 2000:
        return 2000
    if n < 2000:
        if n % 2 == 0:
            return n * (func(n + 1) * 0.5)
        else:
            return n * func(n + 1)

print(func(1998)/func(2001))