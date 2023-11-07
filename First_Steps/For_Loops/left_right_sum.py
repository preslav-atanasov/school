n = int(input("how many numbers in range: "))
count = sum1 = sum2 = 0

for i in range(2 * n):
    num = int(input())
    count += 1
    if count <= 2:
        sum1 += num
    else:
        sum2 += num

if sum1 == sum2:
    print(f"Yes, sum = {sum1}")
else:
    print(f"No, diff = {abs(sum1 - sum2)}")

