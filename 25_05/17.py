file_path = "17.txt"


counter = 0
minn = 100000
maxx = 0
lines = list()
with open(file_path) as f:
    for line in f:
        line = int(line.rstrip("\n"))
        if line % 19 == 0 and line < minn:
            minn = line
        lines.append(line)

for i in range(len(lines) - 1):
    a, b = lines[i], lines[i + 1]
    if a % minn == 0 or b % minn == 0:
       counter += 1
       if (a + b) > maxx:
           maxx = a + b


print(counter, maxx)