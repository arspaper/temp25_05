def func(num):
    bin_num = bin(num)[2:]
    return bin_num.count("1")

print(func(4**12 + 2**32 - 16))