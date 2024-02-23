def ispassvalid(thispasswordinput):
    digitcount = 0
    for char in thispasswordinput:
        if char.isdigit():
            digitcount += 1
    if not (6 <= len(thispasswordinput) <= 10):
        print("Password must be between 6 and 10 characters.")
    if not (thispasswordinput.isalnum()):
        print("Password must consist only of letters and digits.")
    if not (digitcount >= 2):
        print("Password must have at least 2 digits.")
    if 6 <= len(thispasswordinput) <= 10 and thispasswordinput.isalnum() and digitcount >= 2:
        print("Password is valid!")


ispassvalid(thispasswordinput=input())






