"""This module defines the Shape class."""

__author__ = "Michael Obikwere"
__version__ = "1.0.0"

from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, color: str):

        if len(color.strip()) > 0:
            self._color = color
        else:
            raise ValueError ("Color cannot be blank.")
        
    def __str__(self):
        
        return (f"The shape color is {self._color}.")
    
    @abstractmethod
    def calculate_area() -> float:

        pass

    @abstractmethod
    def calculate_perimeter() -> float:

        pass