#!/usr/bin/env python3
# -----------------------------------------------------------
#  Implements a class that represents a single circle.
# -----------------------------------------------------------
import math

class Circle(object):

    def __init__(self, radius=1.0):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2.0

    @diameter.setter
    def diameter(self, val):
        self.radius = val / 2.0

    @property
    def area(self):
        return math.pi * self.radius**2

    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter / 2.0
        return cls(radius)

    def __str__(self):
        return f"Circle with radius: {self.radius}"

    def __repr__(self):
        return f"Circle({self.radius})"
