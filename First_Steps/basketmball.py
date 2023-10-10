ytax = int(input("Godishna taksa za trenirovki po basket "))

# Razlichna basketbolna ekipirovka
bs = ytax - (ytax*40)/100
bt = bs - (bs*20)/100
bb = bt / 4
ba = bb / 5

sum = ytax + bs + bt + bb + ba

print(f"Razhodite na Djesi ako zapochne da trenira basket shte sa {sum}")