from shape import Shape

class Circle(Shape):

    def __init__(self, r):
        if r < 0:
            raise ValueError("Circle radius can't be negative")
        self.r = r
        
    def get_area(self):
        import math
        return math.pi * self.r ** 2

    def get_perimeter(self):
        import math
        return 2 * math.pi * self.r

    def __str__(self):
        return f"Circle with radius: {self.r}"

    @classmethod
    def get_area_formula(cls):
        return "πr^2"

    @classmethod
    def get_perimeter_formula(cls):
        return "2πr"
    
    