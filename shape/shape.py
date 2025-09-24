"""This module defines the Shape class."""

__author__ = "Michael Obikwere"
__version__ = "1.0.0"

from abc import ABC, abstractmethod

class Shape(ABC):
    """
    Shape super class: Maintains shape color.
    """

    def __init__(self, color: str):

        """
        Initializes class attributes to corresponding argument value.

        Args:
            color (str): Represents the color of the Shape.

        Raises:
            ValueError: When color is blank.

        """

        if len(color.strip()) > 0:
            self._color = color
        else:
            raise ValueError ("Color cannot be blank.")
        
    def __str__(self):

        """
        Returns a string representation of the shapes color.

        Returns:
            str: The color of the shape as a string.
        """
        
        return (f"The shape color is {self._color}.")
    
    @abstractmethod
    def calculate_area() -> float:

        """
        Abstract method.
        Implemented in subclass(es).
        """

        pass

    @abstractmethod
    def calculate_perimeter(self) -> float:

        """
        Abstract method.
        Implemented in subclass(es).
        """
        
        pass