userInput = list(input())
wordDictionary = {}

for letter in userInput:
    if letter in wordDictionary:
        wordDictionary[letter] += 1
    else:
        wordDictionary[letter] = 1

for letter, value in wordDictionary.items():
    print(f"{letter} -> {value}")


