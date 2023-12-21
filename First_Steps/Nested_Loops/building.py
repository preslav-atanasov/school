floorNum = int(input("kolko etaji: "))
firstFloor = floorNum
roomNum = int(input("kolko stai na etaj: "))
dedicatedRoomNum = 0
letter = "L"

while floorNum > 0:
    room_counter = 0
    while room_counter < roomNum:
        if firstFloor == floorNum:
            print(f"{letter}{floorNum}{dedicatedRoomNum}", end=" ")
        elif floorNum % 2 == 0:
            letter = "O"
            print(f"{letter}{floorNum}{dedicatedRoomNum}", end=" ")
        elif floorNum % 2 != 0:
            letter = "A"
            print(f"{letter}{floorNum}{dedicatedRoomNum}", end=" ")
        dedicatedRoomNum += 1
        room_counter += 1
    dedicatedRoomNum = 0
    print()
    floorNum -= 1
