import sys

n = int(input("kolko chisla vuv range"))
min_num = -sys.maxsize
max_num = sys.maxsize

for i in range(n):
    numbers = int(input())
    if numbers > min_num:
        min_num = numbers
    if numbers < max_num:
        max_num = numbers

print(f"Min number: {max_num}")
print(f"Max number: {min_num}")




