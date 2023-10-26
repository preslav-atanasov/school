city = str(input("Molq vuvedete grad: "))
earnings = float(input("Molq vuvedete pechalbi: "))

if city == "Sofia":
    if 0 <= earnings <= 500:
        earnings *= 0.05
    elif 500 <= earnings <= 1000:
        earnings *= 0.07
    elif 1000 <= earnings <= 10000:
        earnings *= 0.08
    elif earnings > 10000:
        earnings *= 0.12
    else:
        print("error")
elif city == "Varna":
    if 0 <= earnings <= 500:
        earnings *= 0.045
    elif 500 <= earnings <= 1000:
        earnings *= 0.075
    elif 1000 <= earnings <= 10000:
        earnings *= 0.10
    elif earnings > 10000:
        earnings *= 0.13
    else:
        print("error")
elif city == "Plovdiv":
    if 0 <= earnings <= 500:
        earnings *= 0.055
    elif 500 <= earnings <= 1000:
        earnings *= 0.08
    elif 1000 <= earnings <= 10000:
        earnings *= 0.012
    elif earnings > 10000:
        earnings *= 0.145
    else:
        print("error")
else:
    print("error")
    exit()

print(f"{earnings:.2f}")

