from shape import Shape
from math import sqrt

class Pentagon(Shape):

    def __init__(self, a):
        self.a=a
        ...

    def get_area(self):
        return (1/4) * sqrt(5 * (5 + 2 * sqrt(5))) * self.a ** 2

    def get_perimeter(self):
        return 5 * self.a

    def __str__(self):
        return (f"Pentagon with side {self.a:.2f}, Area: {self.get_area():.2f}, "
                f"Perimeter: {self.get_perimeter():.2f}")

    @classmethod
    def get_area_formula(cls):
        return "1/4 * sqrt(5 * (5 + 2 * sqrt(5))) * a^2"

    @classmethod
    def get_perimeter_formula(cls):
        return "5 * a"