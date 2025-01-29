import abc
from abc import ABC, abstractmethod
from math import pi, sqrt


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def print(self):
        print(f"Printing {self.__class__.__name__}")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius


class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * self.height + 2 * self.width


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2  # Semi-perimeter
        return sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c


circle = Circle(5)
print(circle.area())
print(circle.perimeter())

rectangle = Rectangle(10, 20)
print(rectangle.area())
print(rectangle.perimeter())

triangle = Triangle(3, 4, 5)
print(triangle.area())
print(triangle.perimeter())
