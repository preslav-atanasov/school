# Razmeri
l = float(input("Kakva e duljinata na akvariuma v cm "))
w = float(input("Kakva e shirochinata na akvariuma v cm" ))
h = float(input("Kakva e visochinata na akvariuma v cm "))
per = float(input("Kolko % zaeti ot pqsuk, t.n")) / 100

# Calculation
vol = l * w * h
lvol = vol * 0.001
ln = lvol * (1 - per)

# Result
print(f"Shte sa nujni {ln} litri voda")