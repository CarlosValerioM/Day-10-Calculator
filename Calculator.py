#!/usr/bin/env python3
"""
calculator.py - A simple calculator for basic arithmetic operations.

Author: Carlos Valerio (CarlosValerioM)
Date: 2025/03/17
License: MIT
Dependencies: None (built-in functions only)

Description:
This script performs basic arithmetic operations on two operands.
It takes the following user inputs:
1. The first operand (a number).
2. The second operand (a number).
3. The operation to perform (+, -, *, /).

The script then calculates and displays the result of the operation.

Usage:
Run the script and follow the prompts:
    python calculator.py

Example Output:
    Enter the first operand: 5
    Enter the second operand: 3
    Enter the operation (+, -, *, /): +
    The result is: 8
"""

def main():
    """Simple calculator that takes two operands and an operator to perform basic arithmetic operations."""

    # Get user input for operands and operator
    try:
        operand1 = int(input("Enter the first operand: "))
        operand2 = int(input("Enter the second operand: "))
    except ValueError:
        print("Error: Please enter valid integers.")
        return  # Exit the function if input is invalid

    operator = input("Enter the operation (+, -, *, /): ")

    # Dictionary mapping operators to lambda functions
    operations = {
        "+": lambda first, second: first + second,
        "-": lambda first, second: first - second,
        "*": lambda first, second: first * second,
        "/": lambda first, second: first / second if second != 0 else "Error: Division by zero"
    }

    # Get the corresponding function or return an error message if the operator is invalid
    result = operations.get(operator, lambda a, b: "Error: Invalid operator")(operand1, operand2)

    print(f"The result is: {result}")

# Ensure the script runs only when executed directly
if __name__ == "__main__":
    main()