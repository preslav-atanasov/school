action = input()
num1 = int(input())
num2 = int(input())
answer = 0


def calculation(defaction, defnum1, defnum2, defanswer):
    if defaction == "subtract":
        defanswer = defnum1 - defnum2
    elif defaction == "addition":
        defanswer = defnum1 + defnum2
    elif defaction == "multiply":
        defanswer = defnum1 * defnum2
    elif defaction == "divide":
        defanswer = int(defnum1 / defnum2)   
    else:
        print("Please enter a valid action.")
        exit()
    return defanswer


print(calculation(action, num1, num2, answer))


