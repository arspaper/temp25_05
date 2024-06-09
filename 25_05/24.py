# digits = [1, 2, 4]
# letters = ['Q', 'R', 'W']


# maxx = 0
# with open("24.txt") as f:
#     line = f.readline()
#     count = 0
#     for i in range(len(line) - 1):
#         a, b = line[i], line[i + 1]
#         count += 1
#         if not((a in digits and b in letters) or (b in digits and a in letters)):
#             maxx = max(maxx, count)
#             count = 0

# print(maxx)