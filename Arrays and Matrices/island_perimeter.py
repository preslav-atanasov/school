rows = int(input())
cols = int(input())
perimeter = 0
matrix = []

for i in range(rows):
    row = input().split()
    matrix.append(row)

for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == "1":
            perimeter += 4
            if i > 0 and matrix[i - 1][j] == "1":
                perimeter -= 2
            if j > 0 and matrix[i][j - 1] == "1":
                perimeter -= 2
    print()

print(perimeter)
