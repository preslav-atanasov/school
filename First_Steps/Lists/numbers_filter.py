numberList = []
filteredList = []

n = int(input("how many numbers: "))

for i in range(1, n + 1):
    number = int(input())
    numberList.append(number)

command = input("Please enter a filter: ")

for number in numberList:
    if command == "even" and number % 2 == 0:
        filteredList.append(number)
    elif command == "odd" and number % 2 != 0:
        filteredList.append(number)
    elif command == "positive" and number >= 0:
        filteredList.append(number)
    elif command == "negative" and number < 0:
        filteredList.append(number)

print(filteredList)

