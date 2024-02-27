def factorial_devision(input_1, input_2):
    input_1_factorial = 1.00
    input_2_factorial = 1.00

    for num in range(1, input_1 + 1):
        input_1_factorial *= num
        input_1 -= 1
    for num in range(1, input_2 + 1):
        input_2_factorial *= num
        input_2 -= 1

    print(f"{input_1_factorial / input_2_factorial:.2f}")


factorial_devision(input_1=int(input()), input_2=int(input()))
