"""
Polymorphism.

Polymorphism allows different classes to be treated as if they were the same type,
while behaving differently depending on the class.

Polymorphism lets call the same method on different objects, and they respond
differently based on their class.

Even though the method is the same, the behavior is different.
"""


class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("Vehicle is starting...")

    def stop(self):
        print("Vehicle is stopping...")


class Car(Vehicle):
    def __init__(self, brand, model, year, number_of_doors):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors

    def start(self):
        print("Car is starting")

    def stop(self):
        print("Car is stopping")


class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, speed):
        super().__init__(brand, model, year)
        self.speed = speed

    def start(self):
        print("Motorcycle is starting")

    def stop(self):
        print("Motorcycle is stopping")


vehicles: list[Vehicle] = [
    Car("Ford", "Focus", 2000, 5),
    Motorcycle("Honda", "Scoopy", 2018, 225),
]

for vehicle in vehicles:
    print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
    vehicle.start()
    vehicle.stop()
