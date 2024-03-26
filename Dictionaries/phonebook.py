phonebook = {}
notFound = []
found = {}
number = 0

while True:
    entry = input()
    if entry.isalnum() is False:
        contact = entry.split("-")
        name = contact[0]
        number = contact[1]
        phonebook[name] = number
    else:
        searchesNum = entry
        break

for search in range(int(searchesNum)):
    nameToSearch = input()
    if nameToSearch not in phonebook:
        notFound.append(nameToSearch)
    else:
        found[nameToSearch] = number
for name in notFound:
    print(f"Contact {name} does not exist.")
for nameToSearch in found:
    print(f"{nameToSearch} -> {number}")


