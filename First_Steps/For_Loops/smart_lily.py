liliAge = int(input("Na kolko godini e Lili: "))
washingmachinePrice = float(input("Cena na peralnqta: "))
toyPrice = int(input("Edinichna cena na igrachka: "))

liliBudget = savedMoney = 0
liliToys = 0

for num in range(1, liliAge+1):
    if num % 2 == 0:
        liliBudget += 10
        savedMoney += liliBudget
        print(savedMoney)
        savedMoney -= 1
    else:
        liliToys += 1

savedMoney += (liliToys * toyPrice)

if savedMoney >= washingmachinePrice:
    print(f"Yes! {savedMoney - washingmachinePrice:.2f}")
else:
    print(f"No! {washingmachinePrice - savedMoney:.2f}")
