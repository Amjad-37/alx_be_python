#!/usr/bin/python3
class Calculator:
    """A simple calculator class demonstrating class and static methods."""
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """A static method to add two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """A class method to multiply two numbers."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
