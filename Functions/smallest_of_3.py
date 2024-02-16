def smallest_of_3(defnum1, defnum2, defnum3, deflowest, defemptylist):
    defemptylist.append(defnum1)
    defemptylist.append(defnum2)
    defemptylist.append(defnum3)
    defemptylist.sort()
    deflowest = defemptylist[0]
    return deflowest


num1 = int(input())
num2 = int(input())
num3 = int(input())
emptylist = []
lowest = 0


print(smallest_of_3(num1, num2, num3, lowest, emptylist))
