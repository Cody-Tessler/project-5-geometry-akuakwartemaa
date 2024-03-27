"""
Implement this class.
Recall that every square is a rectangle.
Therefore the Square class should inherit from the Rectangle class.
Do NOT implement the get_area() and get_perimeter() methods here.
Those methods should be inherited from the parent class.
"""
from rectangle import Rectangle

class Square(Rectangle):

    def __init__(self, a):
        super().__init__(a, a)
        ...

    def __str__(self):
        return (f"Square with side {self.length:.2f}, Area: {self.get_area():.2f}, "
                f"Perimeter: {self.get_perimeter():.2f}")


    @classmethod
    def get_area_formula(cls):
        return "side^2"

    @classmethod
    def get_perimeter_formula(cls):
        return "4 * side"
