#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given number using recursion.

    Parameters:
    n (int): The number to calculate the factorial for.

    Returns:
    int: The factorial result of the number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    # Get the number from command line arguments and print its factorial
    f = factorial(int(sys.argv[1]))
    print(f)
