print('X|Y|Z|W')

for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                expression = (not(x >= z))  or (y == w) or y
                if not expression:
                    print(f'{x}|{y}|{z}|{w}')