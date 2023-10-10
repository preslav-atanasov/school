# Cena na menuta
cmenu = 10.35
fmenu = 12.40
vegmenu = 8.15
delivery = 2.50

# Kolko ot vsqko menu
cmenun = int(input("Broi pileshki menuta "))
fmenun = int(input("Broi menuta s riba "))
vegmenun = int(input("Broi vegitarianski menuta "))

# Kalkulacii ig
sum = (cmenu * cmenun) + (fmenu * fmenun) + (vegmenu * vegmenun)
dessert = sum * 20/100

price = (cmenu * cmenun) + (fmenu * fmenun) + (vegmenu * vegmenun) + dessert + delivery
print(f"Obshtata cena na poruchkata e {price}")
