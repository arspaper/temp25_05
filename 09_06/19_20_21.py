def func1(s, p):  # 1 pile, +1, *3, >= 66, vanya first win, bad case petya, min s
    if p == 3:
        if s >= 66:
            return True
        else:
            return False
    return func1(s + 1, p + 1) or func1(s * 3, p + 1)


print("1")
for s in range(1, 65):
    if func1(s, 1):
        print(s)
        break
print()


def func2(s, p):  # 1 pile, +1, *3, >= 66, petya second win, any case vanya, min max s
    if p == 4:
        if s >= 66:
            return True
        else:
            return False
    if s >= 66:
        return False
    if p % 2 == 0:  # petya's turns
        return func2(s + 1, p + 1) and func2(s * 3, p + 1)
    else:  # vanya's turns
        return func2(s + 1, p + 1) or func2(s * 3, p + 1)


print("2")
for s in range(1, 65):
    if func2(s, 1):
        print(s)
print()


def func2_3(s, p):  # 1 pile, +1, +5, *3, >= 66, vanya first can win, vanya second win, any case petya, min s
    if (p == 3 or p == 5) and s >= 66:
        return True
    if p == 5 and s < 66:
        return False
    if s >= 66:
        return False
    if p % 2 != 0:  # vanya's turns
        return func2_3(s + 1, p + 1) and func2_3(s * 3, p + 1)
    else:  # petya's turns
        return func2_3(s + 1, p + 1) or func2_3(s * 3, p + 1)


def func2_3_1(s, p):  # //this func counts guaranteed win
    if p == 5 and s >= 66:
        return True
    if p == 5 and s < 66:
        return False
    if s >= 66:
        return False
    if p % 2 != 0:  # vanya's turns
        return func2_3(s + 1, p + 1) and func2_3(s * 3, p + 1)
    else:  # petya's turns
        return func2_3(s + 1, p + 1) or func2_3(s * 3, p + 1)


print("2_3")
ans = list()
for s in range(1, 66):
    if func2_3(s, 1):
        ans.append(s)
for s in range(1, 66):
    if func2_3_1(s, 1):
        ans.append(s)
print(min(ans))
print()