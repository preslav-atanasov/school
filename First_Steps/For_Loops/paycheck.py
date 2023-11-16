facebookDeduction = 150
instagramDeduction = 100
redditDeduction = 50

tabsOpen = int(input("Kolko tabove sa otvoreni: "))
paycheck = int(input("Zaplata: "))

for i in range(0, tabsOpen):
    tabIs = input()
    if tabIs == "Facebook":
        paycheck -= facebookDeduction
    elif tabIs == "Instagram":
        paycheck -= instagramDeduction
    elif tabIs == "Reddit":
        paycheck -= redditDeduction

if paycheck <= 0:
    print("You have lost your salary.")
else:
    print(paycheck)