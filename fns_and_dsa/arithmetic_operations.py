#!/usr/bin/python3
def perform_operation(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Cannot divide by zero."
        else:
            return num1 / num2
    else:
        # This part should ideally not be reached if main.py is used
        # but it's good practice to have a fallback.
        return "Invalid operation provided."
