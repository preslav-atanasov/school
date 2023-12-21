destination = input("destinaciq: ")
sumNeeded = float(input("budget nujen: "))
savedMoney = 0

while destination != "End":
    savedMoney += float(input("spesteni: "))
    while savedMoney >= sumNeeded:
        print(f"Going to {destination}!")
        destination = input("destinaciq: ")
        if destination != "End":
            savedMoney = 0
            sumNeeded = float(input("budget nujen : "))
        else:
            break
