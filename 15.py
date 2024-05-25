for a in range(100, 0, -1):
    k = 0
    for x in range(1, 1000):
        if ((not(x % a != 0)) => (not(x % 14 == 0)) => (not(x % 4 != 0))):
            k += 1
    if k == 999:
        print(a)
        break