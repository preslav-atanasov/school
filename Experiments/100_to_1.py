n = int(input("please enter number: "))
m = 7
numsDivisibleBym = 0

for number in range(1, n, +1):
    if number % m == 0:
            numsDivisibleBym += 1
    print(number)
print(f"{numsDivisibleBym} numbers exactly divisible by 7 were found")
