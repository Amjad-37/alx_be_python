#!/usr/bin/python3
num1_str = input("Enter the first number: ")
num2_str = input("Enter the second number: ")
operation = input("Choose the operation (+, -, *, /): ")

num1 = float(num1_str)
num2 = float(num2_str)

if operation == "+":
    result = num1 + num2
    print(f"The result is {result}")
elif operation == "-":
    result = num1 - num2
    print(f"The result is {result}")
elif operation == "*":
    result = num1 * num2
    print(f"The result is {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"The result is {result}")
    else:
        print("Cannot divide by zero.")
else:
    print("Invalid operation selected.")

# match operation:
#    case "+":
#        ...
