userInput = input()
uI_split = userInput.split(", ")
character_dict = {}

for i in uI_split:
    key = i
    value = ord(i)
    character_dict[key] = int(value)

print(character_dict)


