#!/usr/bin/env python3
# -----------------------------------------------------------
# test_circle_class.py
#  uses unittest module to test Circle class module
# -----------------------------------------------------------


import unittest
from io import StringIO
from contextlib import redirect_stdout
from circle_class import Circle

class CircleClassTest(unittest.TestCase):

    def test_circle_init(self):
        c = Circle()
        self.assertEqual(c.radius, 1)
        c = Circle(4)
        self.assertEqual(c.radius, 4)

    def test_diameter(self):
        c = Circle()
        self.assertEqual(c.diameter, 2)
        c = Circle(4)
        self.assertEqual(c.diameter, 8)

    def test_set_diameter(self):
        c = Circle(4)
        c.diameter = 2
        self.assertEqual(c.diameter, 2)
        self.assertEqual(c.radius, 1)

    def test_get_area(self):
        c = Circle(2)
        self.assertAlmostEqual(c.area, 12.5663706, places=7)
        with self.assertRaises(AttributeError):
            c.area = 13

    def test_from_diameter(self):
        c = Circle.from_diameter(8)
        self.assertEqual(c.diameter, 8)
        self.assertEqual(c.radius, 4)

    def test_str_method(self):
        c = Circle()
        f = StringIO()
        with redirect_stdout(f):
            print(c)
        self.assertIn("Circle with radius: 1.", f.getvalue())

    def test_repr_method(self):
        c = Circle()
        self.assertEqual("Circle(1.0)", repr(c))
        d = eval(repr(c))
        self.assertEqual(c.radius, d.radius)


    def test_two_circle_add(self):
        c = Circle(2)
        d = Circle(4)
        self.assertEqual(6, (c + d).radius)
        self.assertEqual(12, (c + d).diameter)
        with self.assertRaises(TypeError):
            d = c + 'Square'

    def test_circle_mul(self):
        c = Circle(3)
        self.assertEqual(9, (c * 3).radius)     # Test __mul__
        with self.assertRaises(TypeError):
            d = c * 'monkey'
        self.assertEqual(9, (3 * c).radius)     # Test __rmul__
        self.assertAlmostEqual(9.00, (3.0 * c).radius, places=2)
