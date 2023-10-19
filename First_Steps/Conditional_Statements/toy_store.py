puzzle = 2.60
doll = 3
bear = 4.10
minion = 8.20
truck = 2

price = float(input("Cena na ekskurziqta: "))
puzzzlenum = int(input("Broi puzeli: "))
dollnum = int(input("Broi govoreshti kukli: "))
bearnum = int(input("Broi plusheni mecheta: "))
minionnum = int(input("Broi minioni: "))
trucknum = int(input("Broi kamioncheta: "))

purchasednum = puzzzlenum + dollnum + bearnum + minionnum + trucknum  # broi i cena na poruchka
purchasedpr =\
    (puzzle * puzzzlenum) + (doll * dollnum) + (bear * bearnum) + (minion * minionnum) + (truck * trucknum)

if purchasednum > 50:  # proverka za otstupka
    purchasedpr = purchasedpr - purchasedpr * 0.25

profit = purchasedpr - purchasedpr * 0.10
formatted = '{:.2f}'.format(profit - price)
formatted2 = '{:.2f}'.format(price - profit)

if price < profit:
    print(f"Yes! {formatted} lv left.")
else:
    print(f"Not enough money! {formatted2} lv left.")
