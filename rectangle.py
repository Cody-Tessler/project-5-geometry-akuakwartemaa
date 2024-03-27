from shape import Shape

class Rectangle(Shape):
    

    def __init__(self, a, b):
        if a <= 0 or b <= 0:
            raise ValueError("Rectangle sides must be positive")
        self.a = a
        self.b = b
        ...

    def get_area(self):
        return self.a*self.b

    def get_perimeter(self):
        return 2*(self.a + self.b)

    def __str__(self):
        return f"Rectangle with length {self.a} and width {self.b}, Area: {self.get_area()}, Perimeter: {self.get_perimeter()}"


    @classmethod
    def get_area_formula(cls):
        return "Length * Width"

    @classmethod
    def get_perimeter_formula(cls):
        return "2 * (Length + Width)"
