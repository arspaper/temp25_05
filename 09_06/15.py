for A in range(0, 100):
    flag = False
    for x in range(15, -100, -1):
        for y in range(30, -100, -1):
            if not (y + 2 * x < A):
                flag = True
                break
        if flag:
            break
    if flag == False:
        print(A)
