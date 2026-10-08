"""Basic arithmetic operations for a simple calculator."""


def add(first, second):
    """Return the sum of two numbers."""
    return first + second


def subtract(first, second):
    """Return the difference of two numbers."""
    return first - second


def multiply(first, second):
    """Return the product of two numbers."""
    return first * second


def divide(first, second):
    """Return the quotient of two numbers."""
    if second == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return first / second
