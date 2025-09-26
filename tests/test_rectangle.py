"""This module defines the TestRectangle class.

Usage: 
    To execute all tests in the terminal execute the following command:

    $ python -m unittest tests/test_rectangle.py
"""

__author__ = "Michael Obikwere"
__version__ = "1.0.0"

import unittest
from shape.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.shape = Rectangle("Red", 8, 10)
    
    def test_init_valid_attributes_set(self):
        # shape = Rectangle("Red", 8, 10)

        self.assertEqual("Red", self.shape._color)
        self.assertEqual(8, self.shape._Rectangle__length)
        self.assertEqual(10, self.shape._Rectangle__width)

    def test_init_blank_color_valueerror_raised(self):
        with self.assertRaises(ValueError):
            shape = Rectangle("", 8, 10)

    def test_init_non_numeric_length_valueerror_raised(self):
        with self.assertRaises(ValueError):
            shape = Rectangle("Red", "8", 10)

    def test_init_non_numeric_width_valueerror_raised(self):
        with self.assertRaises(ValueError):
            shape = Rectangle("Red", 8, "10")

    def test_str_color_and_rectangle_sides_strings_returned(self):
        
        expected = (f"The shape color is Red.\nThis rectangle has four"
                    + f" sides with lengths of 8, 10, 8 and 10 "
                    + f"centimeters.")
        
        self.assertEqual(expected, str(self.shape))

    def test_calculate_area_correct_calcution_returned(self):

        expected = 80
        

        self.assertEqual(expected, Rectangle.calculate_area(self.shape))

    def test_calculate_perimeter_correct_calcution_returned(self):

        expected = 36
        

        self.assertEqual(expected, Rectangle.calculate_perimeter(self.shape))