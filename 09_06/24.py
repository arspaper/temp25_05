separator = ['X', 'Y', 'Z']


def exterminator(line):
    sep = separator.copy()
    while True:
        sep.remove(line[0])
        line[1:]
        if line[0] not in sep:
            break


with open("24.txt") as f:
    line = f.readline()
    for i in range(len(line)):
        if line[i] in separator:
            exterminator(line[i:])
