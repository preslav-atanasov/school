listPositives = []
listNegatives = []
positivesNum = total = 0

n = int(input("how many numbers: "))

for i in range(1, n + 1):
    number = int(input())
    if number < 0:
        listNegatives.append(number)
        total += number
    elif number >= 0:
        listPositives.append(number)
        positivesNum += 1

print(listPositives)
print(listNegatives)
print(f"Count of positives is {positivesNum}")
print(f"Sum of negatives is {total}")