fruit = str(input("molq vuvedete plod : "))
weekday = str(input("molq vuvedete den ot sedmicata : "))
quantity = float(input("molq vuvedete kolichestvo : "))

fruit_pr_weekday = {
    "banana": 2.50,
    "apple": 1.20,
    "orange": 0.85,
    "grapefruit": 1.45,
    "kiwi": 2.70,
    "pineapple": 5.50,
    "grapes": 3.85
}

fruit_pr_weekend = {
    "banana": 2.70,
    "apple": 1.25,
    "orange": 0.90,
    "grapefruit": 1.60,
    "kiwi": 3.00,
    "pineapple": 5.60,
    "grapes": 4.20
}

if weekday.lower() in ["monday", "tuesday", "wednesday", "thursday", "friday"]:
    price = fruit_pr_weekday.get(fruit.lower(), "invalid")
    print("{:.2f}".format(price * quantity))
elif weekday in ["saturday", "sunday"]:
    price = fruit_pr_weekend.get(fruit.lower(), "invalid")
    print("{:.2f}".format(price * quantity))
else:
    print("please enter a valid weekday")
