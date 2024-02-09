inputNumbers = input()
numbersAsStrings = inputNumbers.split()
numbers = []

for numString in numbersAsStrings:
    num = int(numString)
    numbers.append(num * -1)

print(numbers)
