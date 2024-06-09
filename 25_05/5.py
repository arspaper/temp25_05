def func(num):
    bin_num = bin(num)[2:]
    if num % 2 == 0:
        bin_num = '10' + bin_num
    else:
        bin_num = '1' + bin_num + '01'
    return int(bin_num, 2)


# myList = list()
for i in range(100):
    result = func(i)
    if result > 516:
        print(i)