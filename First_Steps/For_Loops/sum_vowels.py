count = 0

inputWord = input("Molq vuvedete duma: ")

for char in inputWord:
    if char == "a":
        count += 1
    elif char == "e":
        count += 2
    elif char == "i":
        count += 3
    elif char == "o":
        count += 4
    elif char == "u":
        count += 5

print(count)


