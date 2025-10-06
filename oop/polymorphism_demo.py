#!/usr/-bin/python3
import math

class Shape:
    """Base class for all shapes."""
    def area(self):
        """Calculates the area of the shape. Must be overridden by subclasses."""
        raise NotImplementedError("Subclasses should implement this method.")

class Rectangle(Shape):
    """Represents a rectangle, inheriting from Shape."""
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Overrides the base area method to calculate the rectangle's area."""
        return self.length * self.width

class Circle(Shape):
    """Represents a circle, inheriting from Shape."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Overrides the base area method to calculate the circle's area."""
        return math.pi * (self.radius ** 2)
