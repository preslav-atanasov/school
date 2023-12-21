list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [10, 1, 13, 4, 5, 11]

for num in list1:
    if num in list2:
        print(f"{num} е в двата списъка.")
    else:
        print(f"{num} е само в първия списък.")
