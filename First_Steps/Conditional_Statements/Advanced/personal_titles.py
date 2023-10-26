age = float(input("Molq vuvedete vuzrast : "))
gender = str(input("Molq vuvedete pol (m/n) : "))

if gender == "m":
    if age >= 16:
        print("Mr.")
    else:
        print("Master")
elif gender == "f":
    if age >= 16:
        print("Ms.")
    else:
        print("Miss")
