from collections import Counter

rows = int(input())
cols = int(input())
matrix = []

travelled = 0

for i in range(rows):
    row = input().split()
    for element in row:
        if element not in (".", "#", "S", "E"):
            print("please enter a valid labyrinth.")
            exit()
    matrix.append(row)

for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == "S":
            if matrix[i-1][j]:
                travelled +=1










