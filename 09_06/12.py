def func(line):
    while "01" in line or "02" in line or "03" in line:
        line = line.replace("01", "30", 1)
        line = line.replace("02", "101", 1)
        line = line.replace("03", "202", 1)
    count1 = line.count("1")
    count2 = line.count("2")
    count3 = line.count("3")
    if count1 == 15 and count2 == 10 and count3 == 60:
        return True


for one in range(1, 120):
    print(one)
    for two in range(1, 120):
        for three in range(1, 120):
            line = "0" + "1" * one + "2" * two + "3" * three
            if func(line):
                print()
                print(one)
                break