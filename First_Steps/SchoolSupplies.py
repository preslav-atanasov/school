# Promenlivi (ceni)
pens = 5.80
markers = 7.20
cleaner = 1.20

# Zaqvki
pens_n = float(input("Kolko himikala: "))
markers_n = float(input("Kolko markera: "))
cleaner_n = float(input("Kolko litra preparat: "))
sale = float(input("Kolko % namalenie: ")) / 100

# Namaleni ceni
pens_sale = ((pens * pens_n) - (pens * pens_n) * sale)
markers_sale = ((markers * markers_n) - (markers * markers_n) * sale)
cleaner_sale = ((cleaner * cleaner_n) - (cleaner * cleaner_n) * sale)

# Resultat
result = pens_sale + markers_sale + cleaner_sale
print(F"Na anito she sa i nujni {result} leva")


