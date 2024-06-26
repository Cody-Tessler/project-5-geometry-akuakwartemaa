"""
Implement the get_largest_shape_by_perimeter and get_largest_shape_by_area methods.
"""

from texttable import Texttable
from shape import Shape


class ShapeList:

    def __init__(self):
        """
        Constructs a ShapeList object
        """
        self.shapes = []

    def add_shape(self, shape):
        """
        Adds shape to shapes list. This method check if shape's has Shape class as it's ancestor.
        If not it aise TypeError.
        :param shape: Shape -> Shape class object
        """
        if not isinstance(shape, Shape):
            raise TypeError
        self.shapes.append(shape)

    def get_shapes_table(self):
        """
        This method returns shapes list as string formatted into table.
        :return: string -> formatted table
        """
        t = Texttable()
        t.add_rows([['idx', 'Class', '__str__', 'Perimeter', 'Formula', 'Area', 'Formula']] +
                   [[self.shapes.index(s), type(s).__name__, str(s), s.get_perimeter(), s.get_perimeter_formula(),
                     s.get_area(), s.get_area_formula()] for s in self.shapes])
        return t.draw()

    def get_largest_shape_by_perimeter(self):
        """
        Returns shape with largest perimeter.
        :return: Shape -> object with largest perimeter
        """
        if not self.shapes:
            return None
        max_shape = max(self.shapes, key=lambda shape: shape.get_perimeter())
        return max_shape

    def get_largest_shape_by_area(self):
        """
        Returns shape with largest area.
        :return: Shape -> object with largest area
        """
        if not self.shapes:
            return None
        max_shape = max(self.shapes, key=lambda shape: shape.get_area())
        return max_shape

        
