"""
Calculator Module - Basic arithmetic operations
Students will extend this with more functions
"""

import math  # Import the math module for sqrt


def add(a, b):
    """Add two numbers together"""
    return a + b


def subtract(a, b):
    """Subtract b from a"""
    return a - b


def multiply(a, b):
    """Multiply two numbers with input validation."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a * b


def divide(a, b):
    """Divide a by b with enhanced error handling."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Division requires numeric inputs")
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(a, b):
    """Calculate a to the power of b."""
    if not all(isinstance(i, (int, float)) for i in [a, b]):
        raise TypeError("Inputs must be numbers")
    return a**b


def square_root(a):
    """Calculate the square root of a number."""
    if not isinstance(a, (int, float)):
        raise TypeError("Input must be a number")
    if a < 0:
        raise ValueError("Cannot calculate the square root of a negative number")
    return math.sqrt(a)


# This block lets you test the functions when you run the file directly
if __name__ == "__main__":
    print("🧮 Calculator Module")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")
    print(f"3 * 4 = {multiply(3, 4)}")
    print(f"10 / 2 = {divide(10, 2)}")
    print(f"2^3 = {power(2, 3)}")
    print(f"sqrt(16) = {square_root(16)}")
