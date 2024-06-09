for a in range(10000, 0, -1):
    k = 0
    for x in range(1, 1000):
        if ((x % a != 0) <= ((x % 14 == 0) <= (x % 4 != 0))) == 1:
            k += 1
    if k == 999:
        print(a)
        break