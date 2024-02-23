import sys

userinput = input()
numlist = [int(x) for x in userinput.split()]
smallestNum = sys.maxsize
biggestNum = sys.maxsize * -1
numSum = 0
for num in numlist:
    numSum += num


for i in numlist:
    if i < smallestNum:
        smallestNum = i
for j in numlist:
    if j > biggestNum:
        biggestNum = j

print(f"The minimum number is: {smallestNum}")
print(f"The maximum number is: {biggestNum}")
print(f"The sum number is: {numSum}")
