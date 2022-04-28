import Shape
from cmath import pi

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 2*pi*self.radius

    def calculate_perimeter(self):
        return pi*self.radius*self.radius
