#!/usr/bin/python3
size_str = input("Enter the size of the pattern: ")
size = int(size_str)

row = 0
while row < size:
    for _ in range(size):
        print("*", end="")
    print()
    row += 1
