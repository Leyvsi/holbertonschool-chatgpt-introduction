#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function to calculate the factorial of a number recursively.

    Parameters:
    n (int): The number for which to calculate the factorial. Should be a non-negative integer.

    Returns:
    int: The factorial of the given number n. Returns 1 if n is 0.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Calculate factorial of the number provided as a command-line argument
f = factorial(int(sys.argv[1]))

# Print the result
print(f)
