list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
list3 = [11, 12, 13, 14, 15]
list4 = [16, 17, 18, 19, 20]
list5 = [21, 22, 23, 24, 25]

listFull = [list1, list2, list3, list4, list5]

# Displaying the original lists
for lst in listFull:
    print(lst)

xCoord = int(input("Enter x coordinate to remove (starting from 0): "))
yCoord = int(input("Enter y coordinate to remove (starting from 0): "))

for lst in listFull:
    del listFull[yCoord]
    print(lst)
