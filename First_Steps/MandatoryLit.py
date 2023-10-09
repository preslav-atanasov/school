page_amt = float(input("Broi stranici: "))
pagesph = float(input("Kolko stranici chetete v ramkite na 1 chas: "))
days = float(input("Kolko dni imate za da prochetete knigite: "))

hpd = page_amt / pagesph
hours_needed = hpd / days

print(F"Joro shte trqbva da chete po {hours_needed} chasa na den za da si prochete knijkite")