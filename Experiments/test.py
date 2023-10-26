userInput = input("please enter a list of numbers seperated by a space ")
numberStrings = userInput.split()

listToCheck = [int(i) for i in numberStrings]

if len(listToCheck) < 2:
    print("list is too short.")
    exit()
else:
    listToCheck.sort()

secondLargest = listToCheck[-2]
print(secondLargest)
