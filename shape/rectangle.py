"""This module defines the Rectangle class."""

__author__ = "Michael Obikwere"
__version__ = "1.0.0"

from shape.shape import Shape

class Rectangle(Shape):

    def __init__(self, color: str, length: int, width: int):

        super().__init__(color)

        if isinstance(length, int):
            self.__length = length
        else:
            raise ValueError("Length must be numeric.")
        
        if isinstance(width, int):
            self.__width = width
        else:
            raise ValueError("Width must be numeric.")

    def __str__(self):

        shape_string = super().__str__()
        rectangle_string = (f"\nThis rectangle has four sides length of"
                            + f" {self.__length}, {self.__width}, "
                            + f"{self.__length} and {self.__width} "
                            + f"centimeters.")
        
        return (shape_string + rectangle_string)
    
    def calculate_area(self):

        area = self.__length * self.__width

        return area
    
    def calculate_perimeter(self):

        perimeter = (self.__length *2) + (self.__width * 2)
        
        return perimeter