change = round(float(input("resto: ")) * 100)
count = 0

while change > 0:
    if change >= 200:
        change -= 200
    elif change >= 100:
        change -= 100
    elif change >= 50:
        change -= 50
    elif change >= 20:
        change -= 20
    elif change >= 10:
        change -= 10
    elif change >= 5:
        change -= 5
    elif change >= 2:
        change -= 2
    elif change >= 1:
        change -= 1
    count += 1  # sledim broq na monetite

print(count)    # printirame broqt na monetite
