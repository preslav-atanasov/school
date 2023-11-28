cakeLength = int(input("duljina: "))
cakeWidth = int(input("shirochina: "))
cakeParts = cakeLength * cakeWidth
count = 0

while cakeParts > 0:
    taken = str(input(""))
    if taken == "STOP":
        print(f"{cakeParts} pieces are left.")
        break
    cakeParts -= int(taken)

if cakeParts < 0:
    print(f"No more cake left! You need {abs(cakeParts)} pieces more.")
elif cakeParts == 0:
    print(f"{cakeParts} pieces are left.")
