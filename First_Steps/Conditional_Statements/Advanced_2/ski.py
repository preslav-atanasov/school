roomForOne = 18.00
apartment = 25.00
presidentApartment = 35.00
price = 0

daysNum = int(input("How many days stay: ")) - 1
accomodationType = input("Accomodation type (room for one person, apartment, president apartment): ")
rating = input("Rating (positive/negative): ")


if accomodationType == "room for one person":
    price = roomForOne * daysNum

if accomodationType == "apartment":
    price = apartment * daysNum
    if daysNum < 10:
        price -= price * 0.30
    elif 10 <= daysNum <= 15:
        price -= price * 0.35
    else:
        price -= price * 0.50

if accomodationType == "president apartment":
    price = presidentApartment * daysNum
    if daysNum < 10:
        price -= price * 0.10
    elif 10 <= daysNum <= 15:
        price -= price * 0.15
    else:
        price -= price * 0.20

if rating == "positive":
    price += price * 0.25
elif rating == "negative":
    price -= price * 0.10

print(f"{price:.2f}")
