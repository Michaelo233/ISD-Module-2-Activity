"""This module defines the TestTriangle class.

Usage: 
    To execute all tests in the terminal execute the following command:

    $ python -m unittest tests/test_triangle.py
"""

__author__ = "Michael Obikwere"
__version__ = "1.0.0"

import unittest
from shape.triangle import Triangle

class TestTriangle(unittest.TestCase):

    def setUp(self):
        self.shape = Triangle("Blue", 5, 5, 7)
    
    def test_init_valid_attributes_set(self):
        shape = Triangle("blue", 5, 5, 7)

        self.assertEqual("blue", shape._color)
        self.assertEqual(5, shape._Triangle__side_1)
        self.assertEqual(5, shape._Triangle__side_2)
        self.assertEqual(7, shape._Triangle__side_3)

    def test_init_blank_color_valueerror_raised(self):
        with self.assertRaises(ValueError):
            shape = Triangle("", 5, 5, 7)

    def test_init_non_numeric_side_1_valueerror_raised(self):
        with self.assertRaises(ValueError):
            shape = Triangle("blue", "5", 5, 7)

    def test_init_non_numeric_side_2_valueerror_raised(self):
        with self.assertRaises(ValueError):
            shape = Triangle("blue", 5, "5", 7)

    def test_init_non_numeric_side_3_valueerror_raised(self):
        with self.assertRaises(ValueError):
            shape = Triangle("blue", 5, 5, "7")

    def test_str_color_and_triangle_sides_strings_returned(self):
        
        expected = (f"The shape color is Blue.\nThis triangle has three"
                    + f" sides with lengths of 5, 5, 7 centimeters.")
        
        self.assertEqual(expected, str(self.shape))

    def test_calculate_area_correct_calcution_returned(self):

        expected = 12.497499749949988
        

        self.assertEqual(expected, Triangle.calculate_area(self.shape))

    def test_calculate_perimeter_correct_calcution_returned(self):

        expected = 17
        

        self.assertEqual(expected, Triangle.calculate_perimeter(self.shape))