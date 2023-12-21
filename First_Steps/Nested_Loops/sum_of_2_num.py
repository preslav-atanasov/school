startOfInterval = int(input("start of interval: "))
endOfInterval = int(input("end of interval: "))
magicNumber = int(input("magic number: "))
count = 0


for x1 in range(startOfInterval, endOfInterval + 1):
    for x2 in range(startOfInterval, endOfInterval + 1):
        count += 1
        if x1 + x2 == magicNumber:
            print(f"Combination N:{count} ({x1} + {x2} = {magicNumber})")
            exit()

print(f"{count} combinations - neither equals {magicNumber}")

