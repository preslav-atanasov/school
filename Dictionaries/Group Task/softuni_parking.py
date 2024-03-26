howManyInputs = int(input(f"How many inputs? "))
carDic = {}

for inputs in range(howManyInputs):
    userInput = input("register/unregister {username} {license_plate_number}: ").split()
    if userInput[0] == "register":
        if userInput[1] not in carDic:
            carDic[userInput[1]] = userInput[2]
        else:
            print(f"ERROR: already registered with plate number {userInput[2]}")
    elif userInput[0] == "unregister":
        if userInput[1] in carDic:
            carDic.pop(userInput[1])
            print(f"{userInput[1]} unregistered succesfully")
        else:
            print(f"ERROR: user {userInput[1]} not found")
    else:
        "please enter valid input !!!!"
        exit()

for user in carDic:
    print(f"{user} => {carDic.get(user)}")

