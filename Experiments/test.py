import numpy as np
from scipy.optimize import root_scalar


# Define the function f(x) = x^(a^x) - a^(x^a)
def f(x, a):
    return x ** (a ** x) - a ** (x ** a)


# Define a function to find the root using scipy.optimize
def find_root(a):
    # Define the function f(x) with a fixed parameter a
    func = lambda x: f(x, a)

    # Find the root using the brentq method (which is a root-finding algorithm)
    sol = root_scalar(func, bracket=[0.1, 10])  # Initial bracket guess

    if sol.converged:
        return sol.root
    else:
        return None


# Test for a = 0.5
a = 0.5
root = find_root(a)

if root is not None:
    print(f"Approximate solution for a = {a}: x = {root}")
else:
    print("Unable to find the solution.")