class Vehicle:
    def __init__(self, name: str, color: str, price: int):
        self.name = name
        self.color = color
        self.price = price
        self._gears = 0
        self._current_gear = 0

    def __repr__(self):
        return f"The vehicle is a/an {self.name}, color: {self.color}, price: {self.price}"


# Concrete implementation for Car
class Car(Vehicle):
    @property
    def gears(self):
        return self._gears

    @gears.setter
    def gears(self, value: int):
        if value < 0:
            raise ValueError("Number of gears cannot be negative!")
        self._gears = value

    @property
    def current_gear(self):
        return self._current_gear

    @current_gear.setter
    def current_gear(self, new_gear):
        if 1 <= new_gear <= self._gears:
            self._current_gear = new_gear
        else:
            raise ValueError("Gear is out of range!")


# Concrete implementation for Truck
class Truck(Vehicle):
    @property
    def gears(self):
        return self._gears

    @gears.setter
    def gears(self, value: int):
        if value < 0:
            raise ValueError("Number of gears cannot be negative!")
        self._gears = value

    @property
    def current_gear(self):
        return self._current_gear

    @current_gear.setter
    def current_gear(self, new_gear):
        if 1 <= new_gear <= self._gears:
            self._current_gear = new_gear
        else:
            raise ValueError("Gear is out of range!")


# Example usage
car = Car("Sedan", "Red", 20000)
car.gears = 6  # Setting the number of gears
print(car.gears)  # Getting the number of gears

car.current_gear = 3  # Setting the current gear
print(car.current_gear)  # Getting the current gear

print(car)  # Using the __repr__ method
