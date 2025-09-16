#!/usr/bin/python3
num1_str = input("Enter the first number: ")
num2_str = input("Enter the second number: ")
operation = input("Choose the operation (+, -, *, /): ")

num1 = float(num1_str)
num2 = float(num2_str)

result = None

match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Cannot divide by zero."
    case _:
        result = "Invalid operation selected."

if isinstance(result, str):
    print(result)
else:
    print(f"The result is {result}")
