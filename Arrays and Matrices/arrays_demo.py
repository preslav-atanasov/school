row, col = map(int, input().split(", "))
matrix = []
total_sum = 0

for _ in range(row):
    current_list = []
    elements = input().split(", ")
    for element in elements:
        num = int(element)
        current_list.append(num)
    matrix.append(current_list)

print(matrix)
