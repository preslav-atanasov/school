# Prices
nylonpsqm = 1.50
paintpl = 14.50
pthinnerpl = 5.00
bags = 0.40
nylonadded = 2


# Input
nylonamt = int(input("Kolichestvo nailon "))
paintamt = int(input("Kolichestvo boq (litri) "))
thinneramt = int(input("Kolichestvo razreditel (litri) "))
hours = int(input("Kolko chasove "))

# Sum of materials
sumnylon = (nylonamt + nylonadded) * nylonpsqm
sumpaint = (paintamt + paintamt*10/100) * paintpl
sumthinner = pthinnerpl * thinneramt
osum = sumnylon + sumpaint + sumthinner + bags

workpay = (osum * 30/100) * hours

print(f"The final sum is {osum + workpay}")

