freeSpaceLength = int(input("duljina: "))
freeSpaceWidth = int(input("shirochina: "))
freeSpaceHeight = int(input("visochina: "))
freeSpace = freeSpaceWidth * freeSpaceHeight * freeSpaceLength
count = 0

while freeSpace > 0:
    taken = str(input(""))
    if taken == "Done":
        print(f"{freeSpace} Cubic meters left.")
        break
    freeSpace -= int(taken)

if freeSpace < 0:
    print(f"No more free space! You need {abs(freeSpace)} Cubic meters more.")
elif freeSpace == 0:
    print(f"{freeSpace} Cubic meters left.")
