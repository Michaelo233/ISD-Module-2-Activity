"""This module defines the Triangle class."""

__author__ = "Michael Obikwere"
__version__ = "1.0.0"

from shape.shape import Shape
import math

class Triangle(Shape):

    def __init__(self, color: str, side_1: int, side_2: int,
                  side_3: int):
        
        super().__init__(color)

        if isinstance(side_1, int):
            self.__side_1 = side_1
        else:
            raise ValueError("Side 1 must be numeric")

        if isinstance(side_2, int):
            self.__side_2 = side_2
        else:
            raise ValueError("Side 2 must be numeric")

        if isinstance(side_3, int):
            self.__side_3 = side_3
        else:
            raise ValueError("Side 3 must be numeric")

        if (side_1 + side_2 > side_3 
            and side_1 + side_3 > side_2 
            and side_2 + side_3 > side_1):

            self.__side_1 = side_1
            self.__side_2 = side_2
            self.__side_3 = side_3
        else:
            raise ValueError(f"The sides do not satisfy the Triangle "
                             + f"Inequality")
        
    def __str__(self) -> str:
        shape_string = super().__str__()

        triangle_string = (f"\nThis triangle has three sides with "
                + f"lengths of {self.__side_1}, {self.__side_2},"
                + f" {self.__side_3} centimeters.")
        
        return (shape_string + triangle_string)
    
    def calculate_area(self) -> float:
        
        semi_perimeter = ((self.__side_1 + self.__side_2 + self.__side_3)
                           / 2)
        
        sp = semi_perimeter

        calculate_area = (sp * (sp - self.__side_1) * (sp * self.__side_2)
                          * (sp - self.__side_3))

        area =  math.sqrt(calculate_area)

        return float(area)
    
    def calculate_perimeter(self) -> float:

        p = (self.__side_1 + self.__side_2 + self.__side_3)

        perimeter = p

        return float(perimeter) 