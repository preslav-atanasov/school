import math

sn = str(input("Ime na serial? "))
el = int(input("Produljitelnost na epizod? "))
bt = int(input("Produljitelnost na pochivkata? "))

lunch = bt / 8  # vreme za obqd, otdih i ostanalo vreme
relax = bt / 4
tl = bt - (lunch + relax)


if tl >= el:  # proverki dali ostanaloto vreme e dostatuchno
    ft = math.ceil(tl - el)
    print(f"You have enough time to watch {sn} and are left with {ft} minutes free time.")
else:
    ft = math.ceil(el - tl)
    print(f"You don't have enough time to watch {sn}, you need {ft} more minutes.")
