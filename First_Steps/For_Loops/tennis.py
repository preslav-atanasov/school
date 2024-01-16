tours = int(input("kolko turnira: "))
points = int(input("starting points: "))
placementNum = wins = pointsWon = 0

for i in range(0, tours):
    placement = input()
    if placement == "W":
        points += 2000
        pointsWon += 2000
        wins += 1
    elif placement == "F":
        points += 1200
        pointsWon += 1200
    elif placement == "SF":
        points += 720
        pointsWon += 720
    placementNum += 1

print(points)
print(placementNum)
averagePoints = pointsWon / placementNum
percentWon = (wins / placementNum) * 100

print(f"Final points: {points}")
print(f"Average points: {int(averagePoints)}")
print(f"{percentWon}%")
