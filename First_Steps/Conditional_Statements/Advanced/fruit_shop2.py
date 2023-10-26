fruit = str(input("Molq vuvedete plod: "))
weekday = str(input("Molq vuvedete den ot sedmicata: "))
quantity = float(input("Molq vuvedete kolichestvo: "))
price = 0

if weekday in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    if fruit == "banana":
        price = 2.50
    elif fruit == "apple":
        price = 1.20
    elif fruit == "orange":
        price = 0.85
    elif fruit == "grapefruit":
        price = 1.45
    elif fruit == "kiwi":
        price = 2.70
    elif fruit == "pineapple":
        price = 5.50
    elif fruit == "grapes":
        price = 3.85
    else:
        print("error")
        exit()
    print("{:.2f}".format(price * quantity))
elif weekday in ["Saturday", "Sunday"]:
    if fruit == "banana":
        price = 2.70
    elif fruit == "apple":
        price = 1.25
    elif fruit == "orange":
        price = 0.90
    elif fruit == "grapefruit":
        price = 1.60
    elif fruit == "kiwi":
        price = 3.00
    elif fruit == "pineapple":
        price = 5.60
    elif fruit == "grapes":
        price = 4.20
    else:
        print("error")
        exit()
    print("{:.2f}".format(price * quantity))
else:
    print("error")