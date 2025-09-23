#!/usr/bin/python3
def perform_operation(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Cannot divide by zero."
        else:
            return num1 / num2
    # The main.py ensures only valid operations are passed,
    # but a fallback is good practice for robustness.
    # We can omit the final 'else' as the provided main.py
    # handles the input validation implicitly.
