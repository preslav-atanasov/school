budget = float(input("Budget? "))  # budget i broi nujni neshta
n = int(input("Broi videocarti? "))
m = int(input("Broi procesori? "))
p = int(input("Broi ram pamet? "))

np = 250  # cena na vsichko
mp = (n * np) * 0.35
pp = (n * np) * 0.10
fprice = (n * np) + (m * mp) + (p * pp)

if n > m:  # proverka za otstupka
    fprice = fprice - fprice * .15

if budget > fprice:  # proverka za dostatuchen budget
    print("You have {:.2f} leva left!".format(budget - fprice))
else:
    print("Not enough money! You need {:.2f} leva more!".format(fprice - budget))
