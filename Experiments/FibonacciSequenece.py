sequenceLength = int(input("Duljina: "))

fib_sequence1 = 0
fib_sequence2 = 1
for i in range(1, sequenceLength-1):
    placeholder1 = fib_sequence1
    fib_sequence1 = fib_sequence2
    fib_sequence2 = placeholder1 + fib_sequence2
    placeholder2 = fib_sequence2
    print(fib_sequence1, fib_sequence2, placeholder1, placeholder2)