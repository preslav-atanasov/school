budget = int(input("Molq vuvedete budgeta na grupata: "))
currentSeason = input("Molq vuvedete sezona: ")
fishermenNumber = int(input("Molq vuvedete broq ribari: "))

seasonalRent = {
    "Spring": 3000,
    "Summer": 4200,
    "Autumn": 4200,
    "Winter": 2600
}

price = seasonalRent.get(currentSeason)

if fishermenNumber <= 6:
    price -= price * .10
elif 7 <= fishermenNumber <= 11:
    price -= price * .15
else:
    price -= price * .25

if fishermenNumber % 2 == 0 and currentSeason != "Autumn":
    price -= price * 0.05

if budget > price:
    print(f"Yes! You have {budget - price:.2f} leva left.")
else:
    print(f"Not enough money! You need {price - budget:.2f} leva.")
