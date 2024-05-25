from sys import setrecursionlimit

setrecursionlimit(100000)


def func(n):
    if n == 1:
        return 1
    elif n > 1:
        return func(n - 1) * n

print((func(2024) - func(2023))/func(2022))