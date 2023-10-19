budget = float(input("Budget za filma: "))
st = int(input("Broi statisti: "))
clothing = float(input("Ceni za obleklo na edin statist: "))

decor = budget * 0.10
if st > 150:
    clothing = clothing - clothing * 0.10

clothnum = clothing * st

if (decor + clothnum) > budget:
    print("Not enough money!")
    print("Wingard needs {:.2f} leva more.".format((decor + clothnum) - budget))
else:
    print("Action!")
    print("Wingard starts filming with {:.2f} leva left.".format(budget - (decor + clothnum)))
