with open("26.txt") as f:
    pies = f.readlines()
    num = pies.pop(0)
    pies.sort()
    print(pies)
    for i in range(num):
        pass