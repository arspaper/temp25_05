def func1_1(a, s, p):  # 2 piles, +1, *2, >= 59, vanya first win, bad case petya, min s
    if p == 3:
        if a + s >= 59:
            return True
        else:
            return False
    return func1_1(a + 1, s, p + 1) or func1_1(a, s + 1, p + 1)\
        or func1_1(a * 2, s, p + 1) or func1_1(a, s * 2, p + 1)


print("1_1")
for s in range(1, 54):
    if func1_1(5, s, 1):
        print(s)
        break
print()




def func1_2(a, s, p):  # 2 piles, +1, *2, >= 59, petya second win, any case vanya, min max s
    if p == 4:
        if a + s >= 59:
            return True
        else:
            return False
    if a + s >= 59:
        return False
    if p % 2 == 0:  # petya's turns
        return func1_2(a + 1, s, p + 1) and func1_2(a, s + 1, p + 1)\
            and func1_2(a * 2, s, p + 1) and func1_2(a, s * 2, p + 1)
    else:  # vanya's turns
        return func1_2(a + 1, s, p + 1) or func1_2(a, s + 1, p + 1)\
            or func1_2(a * 2, s, p + 1) or func1_2(a, s * 2, p + 1)



print("1_2")
ans = list()
for s in range(1, 53):
    if func1_2(5, s, 1):
        ans.append(s)
print(ans)
print()



def func1_3(a, s, p):  # 2 piles, +1, *2, >= 59, vanya first can win, vanya second win, any case petya, min s
    if (p == 3 or p == 5) and a + s >= 59:
        return True
    if p == 5 and a + s < 59:
        return False
    if a + s >= 59:
        return False
    if p % 2 == 0:  # petya's turns
        return func1_3(a + 1, s, p + 1) or func1_3(a, s + 1, p + 1)\
            or func1_3(a * 2, s, p + 1) or func1_3(a, s * 2, p + 1)
    else:  # vanya's turns
        return func1_3(a + 1, s, p + 1) and func1_3(a, s + 1, p + 1)\
            and func1_3(a * 2, s, p + 1) and func1_3(a, s * 2, p + 1)
    

def func1_3_1(a, s, p):  # this func counts guaranteed win
    if p == 5 and a + s >= 59:
        return True
    if p == 5 and a + s < 59:
        return False
    if a + s >= 59:
        return False
    if p % 2 == 0:  # petya's turns
        return func1_3_1(a + 1, s, p + 1) or func1_3_1(a, s + 1, p + 1)\
            or func1_3_1(a * 2, s, p + 1) or func1_3_1(a, s * 2, p + 1)
    else:  # vanya's turns
        return func1_3_1(a + 1, s, p + 1) and func1_3_1(a, s + 1, p + 1)\
            and func1_3_1(a * 2, s, p + 1) and func1_3_1(a, s * 2, p + 1)


print("1_3")
ans = list()
for s in range(1, 53):
    if func1_3(5, s, 1):
        ans.append(s)
for s in range(1, 53):
    if func1_3_1(5, s, 1):
        ans.append(s)
print(min(ans))
print()