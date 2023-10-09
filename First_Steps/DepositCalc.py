dep_amt = float(input("Molq vuvetedete depoziranata suma: "))
dep_term = float(input("Molq vuvedete srok na depozit vuv meseci: "))
yir = float(input("Molq vuvedete godishniq lihven procent: ")) / 100

eot_amt = dep_amt + dep_term * ((dep_amt * yir) / 12)
print(F"Sumata v kraq na sroka e {eot_amt}")

procent = float(input("kolko procenta")) / 100
asd = float(input("nsht deto go umn po procenta"))
otg = asd * procent

