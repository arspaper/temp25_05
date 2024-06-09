exp = 2 * (729**2014) + 2 * (81 ** 2018) + 2 * (27**2020) - 2 * (9 ** 2022) - 2024
count = 0
while exp != 0:
    if exp % 27 > 9:
        count += 1
    exp //= 27
print(count)