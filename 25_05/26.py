pies = [int(line.strip()) for line in open('26.txt','r')]
num = pies.pop(0)
pies.sort()
count = 1
maxCount = 0
newNum = num

pie = pies[newNum - 1]
newPie = pie - 4
newNum -= 1
outList = list()

while newNum:
    currPie = pies[newNum - 1]
    if currPie <= newPie:
        outList.append(currPie)
        count += 1
        newPie = currPie - 4
    newNum -= 1

print(count, min(outList))