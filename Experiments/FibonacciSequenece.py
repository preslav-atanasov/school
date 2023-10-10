# Function to generate Fibonacci sequence
def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    return fib_sequence

# Specify the number of Fibonacci numbers to generate
n = 1000  # Change this value if you want a different number of Fibonacci numbers

# Generate and print the Fibonacci sequence
print(fibonacci(n))