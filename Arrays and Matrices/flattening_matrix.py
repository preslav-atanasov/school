rows = int(input())
matrix = []

for _ in range(rows):
    current_list = []
    elements = input().split(", ")
    for element in elements:
        matrix.append(element)

print(matrix)