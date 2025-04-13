"""
An Abstract Base Class (ABC) in Python is a template for other classes.
It can't be instantiated on its own - its main role is to enforce structure in subclasses.
Why use ABC?
1. To enforce that all subclasses implement specific behavior.
2. To define a shared interface or "contract" across many classes.
3. To define default logic inside them that subclasses can reuse or override.
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5


shapes: list[Shape] = [Circle(4), Square(5), Triangle(6, 7)]

for shape in shapes:
    print(shape.area())
