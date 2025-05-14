rows = 4
cols = 3
matrix = []

for i in range(rows):
    row = input().split(", ")
    matrix.append(row)

for i in range(rows):
    if i % 2 != 0:
        for j in range(cols):
            print(matrix[i][j], end=" ")
        print()

