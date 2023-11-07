n = int(input("1st num in range "))
m = int(input("last num in range "))
sumOfNaturals = num = 0

for i in range(n, m):
    num += 1
    if isinstance(num, int) and num > 0:
        sumOfNaturals += 1

print(f"Obshto ima {sumOfNaturals} estestveni chisla")

