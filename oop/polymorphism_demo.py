# polymorphism_demo.py

import math

# Base class
class Shape:
    def area(self):
        """Base method to calculate area, must be overridden by subclasses."""
        raise NotImplementedError("Subclasses must override the area() method")


# Derived class for rectangles
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Calculate the area of the rectangle."""
        return self.length * self.width


# Derived class for circles
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return math.pi * (self.radius ** 2)
