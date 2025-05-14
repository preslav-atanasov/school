from math import ceil
board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]

player_1 = None
player_2 = None
current = None
move = 0

def draw():
    print("board:")
    print("⬜⬜⬜")
    print("⬜⬜⬜")
    print("⬜⬜⬜")


def play():
    global board
    global move
    global current
    choice = int(input("Choose a position [1-9]:"))
    row = ceil(choice / 3) - 1
    col = choice % 3 - 1
    if move % 2 == 0:
        board[row][col] = "❌"
        current = "❌"
    else:
        board[row][col] = "⭕"
        current = "❌"
    move += 1
    while True:
        print(board)
        first_row = all(x == current for x in board[0])
        














