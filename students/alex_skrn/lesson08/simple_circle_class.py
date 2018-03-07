#!/usr/bin/python
"""A Simple Circle Class - Week 8 assignment."""

import math
import functools


@functools.total_ordering
class Circle(object):
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("radius must be non-negative")
        self._radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        """Construct a circle from a diameter."""
        return cls(diameter / 2.0)

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, val):
        if val < 0:
            raise ValueError("radius can't be less than 0")
        self._radius = val

    @property
    def diameter(self):
        return 2 * self._radius

    @diameter.setter
    def diameter(self, val):
        self._radius = val / 2.0

    @property
    def area(self):
        return math.pi * self._radius ** 2.0

    def __str__(self):
        return "Circle with radius: {:.6f}".format(float(self._radius))

    def __repr__(self):
        return "Circle({})".format(self._radius)

    def __eq__(self, other):
        return self._radius == other.radius

    def __lt__(self, other):
        return self._radius < other.radius

    def __add__(self, other):
        return Circle(self._radius + other.radius)

    def __mul__(self, scalar):
        return Circle(self._radius * scalar)

    def __rmul__(self, scalar):
        return Circle(self._radius * scalar)

    def __sub__(self, other):
        return Circle(self._radius - other.radius)


class Sphere(Circle):
    @property
    def volume(self):
        return (4/3) * math.pi * (self._radius ** 3)

    def __str__(self):
        return "Sphere with radius: {:.6f}".format(float(self._radius))

    def __repr__(self):
        return "Sphere({})".format(self._radius)
