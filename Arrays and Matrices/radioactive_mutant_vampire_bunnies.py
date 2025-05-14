from collections import Counter

rows = int(input())
cols = int(input())
matrix = []
player_count = 0

x_axis = 0
y_axis = 0



for i in range(rows):
    row = input().split()
    element_counts = Counter(row)
    for element in row:
        if element not in ("B", "P", "."):
            print("please enter a valid lair!")
            exit()

        if element == "P":
            player_count += 1

        if player_count > 1:
            print("More than one player not supported!")
            exit()
    matrix.append(row)

commands = list(input())
for command in commands:
    if command == "L":
        x_axis -= 1
    elif command == "R":
        x_axis += 1
    elif command == "U":
        y_axis -= 1
    elif command == "D":
        y_axis += 1

for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == "P" and commands:
            matrix[i][j] = "."
            matrix[i+y_axis][j+x_axis] = "P"




