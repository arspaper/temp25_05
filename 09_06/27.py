f = [int(line.strip()) for line in open('09_06/27-B.txt','r')]

count = 0
for i in range(len(f) - 1):
    for j in range(i + 1, len(f)):
        a, b = f[i], f[j]
        if (a + b) % 3 == 0 and (a * b) % 2 ** 12 == 0:
            count += 1

print(count)