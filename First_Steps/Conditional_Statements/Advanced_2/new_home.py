flowerType = input("Molq vuvedete vida na cvetqta ")
flowerQuantity = int(input("Molq vuvedete broi cvetq "))
budget = int(input("Molq vuvedete budget "))

flowerPrices = {
    "Roses": 5,
    "Dahlias": 3.80,
    "Tulips": 2.80,
    "Narcissus": 3,
    "Gladiolus": 2.50,
}

finalPrice = flowerQuantity * flowerPrices.get(flowerType)

if flowerType == "Roses" and flowerQuantity > 80:
    finalPrice -= finalPrice * 0.10
elif flowerType == "Dahlias" and flowerQuantity > 90:
    finalPrice -= finalPrice * 0.15
elif flowerType == "Tulips" and flowerQuantity > 80:
    finalPrice -= finalPrice * 0.15
elif flowerType == "Narcissus" and flowerQuantity < 120:
    finalPrice += finalPrice * 0.15
elif flowerType == "Gladiolus" and flowerQuantity < 80:
    finalPrice += finalPrice * 0.20

if finalPrice <= budget:
    print(f"Hey, you have a great garden with {flowerQuantity} {flowerType} and {budget - finalPrice:.2f} leva left.")
else:
    print(f"Not enough money, you need {finalPrice - budget:.2f} leva more.")
