"""This module defines the Rectangle class."""

__author__ = "Michael Obikwere"
__version__ = "1.0.0"

from shape.shape import Shape

class Rectangle(Shape):
    """
    Subclass Rectangle: Rectangle shape class.
    """
    def __init__(self, color: str, length: int, width: int):
        """
        Initializes class attributes to corresponding argument value.

        Args:
            color (str): Represents the color of the Shape.
            length (int): The length of 2 opposing sides of the 
                rectangle.
            width (int): The width of the two opposing sides of the 
                rectangle.

        Raises:
            ValueError: When color is blank, When length is not an int,
                When width is not an int.

        """
         
        super().__init__(color)

        if isinstance(length, int):
            self.__length = length
        else:
            raise ValueError("Length must be numeric.")
        
        if isinstance(width, int):
            self.__width = width
        else:
            raise ValueError("Width must be numeric.")

    def __str__(self) -> str:
        """
        Return string represention of the color, length and width of the
            Rectangle.

        Returns:
            str: The color, length and width of each side of the 
                Rectangle.
        """

        shape_string = super().__str__()
        rectangle_string = (f"\nThis rectangle has four sides length of"
                            + f" {self.__length}, {self.__width}, "
                            + f"{self.__length} and {self.__width} "
                            + f"centimeters.")
        
        return (shape_string + rectangle_string)
    
    def calculate_area(self) -> float:

        """
        Implementing abstract method calculate area.

        Returns:
            float: Area of the rectangle as a float.
        """
        area = self.__length * self.__width

        return float(area)
    
    def calculate_perimeter(self) -> float:

        """
        Implementing abstract method calculate perimeter.

        Returns:
            float: perimeter of the rectangle as a float.
        """

        perimeter = (self.__length *2) + (self.__width * 2)

        return float(perimeter)