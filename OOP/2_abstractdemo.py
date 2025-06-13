"""
2_abstractdemo.py
-----------------
This script demonstrates the concept of abstract classes in Python using the abc module.

Key Concepts:
1. Abstract Base Class (ABC)
2. Abstract methods
3. Enforcing method implementation in subclasses
4. Attempting to instantiate an abstract class

The abc module (Abstract Base Classes) allows you to define abstract classes and methods.
An abstract class cannot be instantiated directly and must be subclassed.
Any subclass must implement all abstract methods, or it will also be abstract.
"""

from abc import ABC, abstractmethod

# Abstract Base Class definition
class Shape(ABC):
    """
    Abstract base class for geometric shapes.
    Any subclass must implement the area() method.
    """

    @abstractmethod
    def area(self):
        """
        Abstract method for calculating area.
        Must be implemented by any subclass of Shape.

        The 'pass' statement is used as a placeholder for future code. Here, it indicates
        that the method has no implementation in the abstract base class, and must be
        implemented by subclasses. If you remove 'pass' and leave the method body empty,
        Python will raise an IndentationError.
        """
        pass

# Concrete subclass implementing the abstract method
class Rectangle(Shape):
    def __init__(self, rect_width, rect_height):
        """
        Constructor for Rectangle.
        Parameters:
            rect_width: The width of the rectangle (passed during object creation)
            rect_height: The height of the rectangle (passed during object creation)
        Instance variables are named self.w and self.h to avoid confusion with parameter names.
        """
        self.w = rect_width      # Instance variable for width
        self.h = rect_height     # Instance variable for height

    def area(self):
        """
        Implementation of the abstract method area().
        Returns the area of the rectangle.
        """
        return self.w * self.h

# Another concrete subclass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """
        Implementation of the abstract method area().
        Returns the area of the circle.
        """
        from math import pi
        return pi * self.radius ** 2

if __name__ == "__main__":
    # Uncommenting the next line will raise an error:
    # TypeError: Can't instantiate abstract class Shape with abstract method area
    # shape = Shape()


    # Create instances of concrete subclasses
    rect = Rectangle(10, 5)
    circ = Circle(7)

    print(f"Rectangle area: {rect.area()}")
    print(f"Circle area: {circ.area()}")

    # Demonstrate that all subclasses must implement area()
    # If a subclass does not implement area(), it cannot be instantiated.
