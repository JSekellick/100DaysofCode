# Jared Sekellick

# Deck of Cards

class Car:
    def __init__():
        self.color = "Red" # ends up on the object
        make = "Mercedes" # becomes a local variable in the constructor

car = Car()
print(car.color) # "Red"
print(car.make) # would result in an error, `make` does not exist on the object

pi = (355/113)

class Elevator:
    def __init__(self, starting_floor):
        self.make = "The Elevator Company"
        self.floor = starting_floor

# To create the object

elevator = Elevator(1)
print(elevator.make)
print(elevator.floor)