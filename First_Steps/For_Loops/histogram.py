n = int(input("Molq vuvedete kolko chisla da budat v histogramata: "))

percent1 = percent2 = percent3 = percent4 = percent5 = 0
count1 = count2 = count3 = count4 = count5 = 0

for i in range(0, n):
    num = int(input())
    if num < 200:
        count1 += 1
        percent1 = count1 / n * 100
    elif 200 <= num <= 399:
        count2 += 1
        percent2 = count2 / n * 100
    elif 400 <= num <= 599:
        count3 += 1
        percent3 = count3 / n * 100
    elif 600 <= num <= 799:
        count4 += 1
        percent4 = count4 / n * 100
    else:
        count5 += 1
        percent5 = count5 / n * 100

print(f"{percent1:.2f}%")
print(f"{percent2:.2f}%")
print(f"{percent3:.2f}%")
print(f"{percent4:.2f}%")
print(f"{percent5:.2f}%")

