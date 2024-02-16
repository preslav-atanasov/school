team_A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
gameTerminated = False

teamInput = input("Red cards given: (TEAM-NUMBER) ")

teamKicks = teamInput.split(" ")
for item in teamKicks:
    itemParts = item.split("-")
    print(item)
    if len(team_A) > 7 and len(team_B) > 7:
        if item[0] == "A":
            team_A.remove(int(itemParts[1]))
        elif item[0] == "B":
            team_B.remove(int(itemParts[1]))
    else:
        gameTerminated = True

print(f"Team A - {len(team_A)}; Team B - {len(team_B)}")
if gameTerminated is True:
    print("Game was terminated")





