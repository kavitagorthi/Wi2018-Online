#!/usr/bin/env python3
# -----------------------------------------------------------
# test_circle_class.py
#  uses unittest module to test Circle class module
# -----------------------------------------------------------


import unittest
from io import StringIO
# from contextlib import redirect_stdout
import circle_class as cc

class CircleClassTest(unittest.TestCase):

    def test_circle_init(self):
        c = cc.Circle()
        self.assertEqual(c.radius, 1)
        c = cc.Circle(4)
        self.assertEqual(c.radius, 4)


