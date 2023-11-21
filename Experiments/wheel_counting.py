"""wheelNum = int(input("broi na kolelata: "))
cars = trucks = motorbikes = 0

if 3 < wheelNum < 50:
    while cars * 4 <= wheelNum:
        trucks = 0
        while trucks * 6 <= wheelNum - (cars * 4):
            motorbikes = 0
            while motorbikes * 3 <= wheelNum - (cars * 4 + trucks * 6):
                if (cars * 4 + trucks * 6 + motorbikes * 3) == wheelNum:
                    print(cars, trucks, motorbikes)
                motorbikes += 1
            trucks += 1
        cars += 1
else:
    print("molq vuvedete broi kolela mejdu 3 i 50")"""

wheelNum = int(input("broi na kolelata: "))
cars = trucks = motorbikes = 0

if 3 < wheelNum < 50:
    for cars in range(wheelNum // 4 + 1):
        trucks = 0
        for trucks in range(wheelNum // 6 + 1):
            motorbikes = 0
            for motorbikes in range(wheelNum // 3 + 1):
                if (cars * 4 + trucks * 6 + motorbikes * 3) == wheelNum:
                    print(cars, trucks, motorbikes)
                motorbikes += 1
            trucks += 1
        cars += 1
else:
    print("molq vuvedete broi kolela mejdu 3 i 50")