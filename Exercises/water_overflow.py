waterCapacity = 255
litersFilled = filledAtLiters = 0


n = int(input("how many times: "))

for i in range(0, n):
    addedLiters = int(input())
    if litersFilled + addedLiters <= 255:
        litersFilled += addedLiters
    else:
        print("Insufficient capacity!")

print(litersFilled)
