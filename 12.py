line = "8" * 82
while "1111" in line or "8888" in line:
    if "1111" in line:
        line = line.replace("1111", "8", 1)
    else:
        line = line.replace("8888", "11", 1)

print(line)