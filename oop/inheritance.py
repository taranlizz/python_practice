"""
Inheritance.
Inheritance is a fundamental concept in OOP that involves creating
new classes (subclasses or derived classes) based on existing classes
(superclasses or base classes).

The IS-A relationship defines when one class is a type of another class.
If class B inherits from class A, and you can say "B is an A",
then it's an IS-A relationship - and inheritance is appropriate.
"""


class Vehicle:
    def __init__(self, brand, model, year, max_speed):
        self.brand = brand
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def describe(self):
        print(
            f"Brand: {self.brand}, model: {self.model}, year: {self.year}, max speed: {self.max_speed}"
        )


class Car(Vehicle):
    def __init__(self, brand, model, year, max_speed, num_doors):
        super().__init__(brand, model, year, max_speed)
        self.num_doors = num_doors


class Bike(Vehicle):
    def __init__(self, brand, model, year, max_speed, num_wheels):
        super().__init__(brand, model, year, max_speed)
        self.num_wheels = num_wheels


car = Car("Ford", "Focus", 2008, 185, 4)
bike = Bike("Urban", "C1 Hybrid", 2022, 60, 2)
