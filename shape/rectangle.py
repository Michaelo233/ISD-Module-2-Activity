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