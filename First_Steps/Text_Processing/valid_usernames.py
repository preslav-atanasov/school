import re

validUsernames = []
userInput = input().split(", ")
pattern = r'^[a-zA-Z0-9_-]+$'

for name in userInput:
    if 3 < len(name) < 16 and re.match(pattern, name):
        validUsernames.append(name)
    else:
        pass

for validname in validUsernames:
    print(validname)
