numsum = 0


def operate(given_tuple):
    global numsum
    operation, *rest = given_tuple
    if operation == "+":
        for n in range(len(rest)):
            numsum += rest[n]
            n += 1
        print(numsum)
    elif operation == "-":
        numsum = rest[0]
        starting_number, *to_remove = rest
        for n in range(len(to_remove)):
            numsum -= to_remove[n]
            n += 1
        print(numsum)
    elif operation == "*":
        numsum = 1
        for n in range(len(rest)):
            numsum *= rest[n]
            n += 1
        print(numsum)
    elif operation == "/":
        numsum = 1
        for n in range(len(rest)):
            numsum /= rest[n]
            n += 1
        print(numsum)


tuple_to_do = ("/", 1, 2, 3)
operate(tuple_to_do)


