#!/usr/bin/python3
number_str = input("Enter a number to see its multiplication table: ")
number = int(number_str)

for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")
