goal = 10000
stepsWalked = 0
keepSteps = 0

while stepsWalked <= goal:
    addSteps = str(input())
    if addSteps == "Going home":
        addSteps = str(input())
        stepsWalked += int(addSteps)
        break
    stepsWalked += int(addSteps)

if stepsWalked >= goal:
    print(f"Goal reached! Good job! {abs(goal - stepsWalked)} steps over the goal!")
elif stepsWalked < goal:
    print(f"{goal - stepsWalked} more steps to reach the goal.")
