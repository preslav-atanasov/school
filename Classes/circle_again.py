class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.area_of_sector = None
        self.area = None
        self.circumfrence = None
        self.diameter = diameter
        self.radius = diameter / 2
        self.angle = int(input("kolko gradusa e sectora za izchislqvane?: "))

    def calculate_circumference(self):
        self.circumfrence = 2 * self.__pi * self.radius
        return self.circumfrence

    def calculate_area(self):
        self.area = self.__pi * (self.radius ** 2)
        return self.area

    def calculate_area_of_sector(self):
        self.area_of_sector = (1/2 * self.radius ** 2) * self.angle
        return self.area_of_sector


circle = Circle(10)
print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector():.2f}")
