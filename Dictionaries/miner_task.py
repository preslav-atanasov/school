ores = {}
value = 0

while True:
    ore = input("Enter ore name (type 'stop' to end): ")
    if ore == "stop":
        break
    value = int(input("Enter value: "))
    quantity = value
    if ore not in ores:
        ores[ore] = 0
    ores[ore] += value


for ore, value in ores.items():
    print(f"{ore} -> {value}")
