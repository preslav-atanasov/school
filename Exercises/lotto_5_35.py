import random

lottonums = [0, 0, 0, 0, 0]

for i in range(len(lottonums)):
    num = random.randrange(1, 35)
    if num not in lottonums:
        lottonums[i] = num

print(lottonums)
