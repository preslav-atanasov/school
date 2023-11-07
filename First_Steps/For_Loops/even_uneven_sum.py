n = int(input("how many numbers in range: "))
count = sum1 = sum2 = 0

for i in range(n):
    num = int(input())
    count += 1
    if count % 2 == 0:
        sum1 += num
    else:
        sum2 += num

if sum1 == sum2:
    print(f"Yes")
    print(f"Sum = {sum1}")
else:
    print(f"No")
    print(f"Diff = {abs(sum1 - sum2)}")

