items = {
    "shards": 0,
    "fragments": 0,
    "motes": 0,
}

obtained = False

while True:
    userInput = input().split(" ")

    for i in range(0, len(userInput), 2):
        item = userInput[i+1]
        quantity = int(userInput[i])

        if item.lower() == "shards":
            items["shards"] += quantity
            if items.get("shards") >= 250:
                print("Shadowmourne obtained!")
                items["shards"] -= 250
                obtained = True
                break

        elif item.lower() == "fragments":
            items["fragments"] += quantity
            if items.get("fragments") >= 250:
                print("Valanyr obtained!")
                items["fragments"] -= 250
                obtained = True
                break

        elif item.lower() == "motes":
            items["motes"] += quantity
            if items.get("motes") >= 250:
                print("Dragonwrath obtained!")
                items["motes"] -= 250
                obtained = True
                break

        elif item.isalpha() and item not in items:
            key = item.lower()
            items.update({str(key): quantity})

    if obtained:
        break

for item in items:
    print(f"{item}: {items.get(item)}")
