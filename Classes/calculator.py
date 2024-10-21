class Calculator:
    def __init__(self, num1: float, num2: float):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        num_sum = self.num1 + self.num2
        print(num_sum)

    def subtract(self):
        num_sub = self.num2 - self.num1
        print(num_sub)

    def multiply(self):
        num_mult = self.num1 * self.num2
        print(num_mult)

    def divide(self):
        if self.num2 == 0:
            print("На 0 не се дели.")
            exit()
        num_divide = self.num1 / self.num2
        print(num_divide)


calc = Calculator(float(input("Число 1: ")), float(input("Число 2: ")))
while True:
    action = input("Изберете действие (add, subtract, multiply, divide): ")
    if action == "add":
        calc.add()
    elif action == "subtract":
        calc.subtract()
    elif action == "multiply":
        calc.multiply()
    elif action == "divide":
        calc.divide()
    else:
        print("Невалидно действие. Моля, опитайте отново.")

