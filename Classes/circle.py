class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = diameter / 2

    def calculate_circumfrence(self):
        return Circle.__pi * self.diameter

    def calculate_area(self):
        return Circle.__pi * self.radius * self.radius

    def calculate_area_of_sector(self, angle):
        return (angle/360) * circle.__pi * self.radius * self.radius


circle = Circle(10)
angle = 30
print(f"{circle.calculate_circumfrence():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")
