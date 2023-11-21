bal = 0
deposit = ""

while deposit != "NoMoreMoney":
    deposit = input()
    if deposit == "NoMoreMoney":
        break
    if float(deposit) < 0:
        print("Invalid operation!")
        break
    bal += float(deposit)
    print(f"Increase: {float(deposit):.2f}")

print(f"Total: {bal:.2f}")