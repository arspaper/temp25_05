def func(num):
    bin_num = bin(num)[2:]
    if bin_num.count("1") % 2 == 0:
        bin_num = "10" + bin_num[2:] + "0"
    else:
        bin_num = "11" + bin_num[2:] + "1"
    return int(bin_num, 2)

for i in range(100):
    result = func(i)
    if result > 40:
        print(i)
        break