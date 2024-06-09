from fnmatch import *
for x in range (0, 10**9, 3123):
    if fnmatch(str(x),'12*63?5?'):
        print(x)

