counter = 0
maxx = 0
lines = list()
f = open("09_06/17.txt")
lines = [int(i) for i in f]

for i in range(len(lines) - 1):
    for j in range(i + 1, len(lines)):
        a, b = lines[i], lines[j]
        if ((a + b) % 80 == 0) and ((a % 50 == 0) or (b % 50 == 0)):
            maxx = max(maxx, a + b)
            counter += 1



print(counter, maxx)

