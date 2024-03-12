elements = input().split(" ")
pantry = {}

for element in range(0, len(elements), 2):
    key = elements[element]     # name of element
    value = elements[element + 1]   # value of element
    pantry[key] = int(value)     # assign every name to a value

searched_items = input().split(" ")

for item in searched_items:
    if item in pantry:
        print(f"We have {pantry[item]} of {item} left.")
    else:
        print(f"Sorry, we don't have {item}")