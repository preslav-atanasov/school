def sum_numbers(defnum1, defnum2):
    defsum = defnum1 + defnum2
    return defsum


def subtract(defnum1, defnum2, defnum3):
    defsum = sum_numbers(defnum1, defnum2)
    defresult = defsum - defnum3
    return defresult


def add_and_subtract(defnum1, defnum2, defnum3):
    defresult = subtract(defnum1, defnum2, defnum3)
    return defresult


num1 = int(input())
num2 = int(input())
num3 = int(input())
sumOfFirst2 = 0


print(add_and_subtract(num1, num2, num3))
