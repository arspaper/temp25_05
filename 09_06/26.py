process = [line.strip().split() for line in open('09_06/26.txt','r')]
num = process.pop(0)

maxx = 0
for timeline in range(1633046400, 1635724717):
    for start, finish in process:
        if start == 0:
            