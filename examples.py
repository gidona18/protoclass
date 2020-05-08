"""
# The Expression Problem

>>> import math
>>> from protoclass import proto, clone

# We need some "legacy code" - data structures and functionality
# Data Structures

>>> circle = proto(r=0.0)
>>> triangle = proto(a=0.0, b=0.0, c=0.0)


# Functionality
>>> def triangle_area(self):
...     a, b, c = self.a, self.b, self.c
...     s = (a + b + c) / 2.0
...     return (s * (s - a) * (s - b) * (s - c)) ** 0.5

>>> triangle.area = triangle_area
>>> circle.area = lambda self: math.pi * self.r ** 2.0


# New functionality
>>> circle.perimeter = lambda self: self.r * 2.0

>>> triangle.perimeter = lambda self: self.a + self.b + self.c


# New data structure and functionality
>>> square = proto(s=0.0)
>>> square.area = lambda self: self.s * self.s

>>> square.perimeter = lambda self: self.s * 4.0


# We can test our code now

>>> test_square = clone(square)
>>> test_square.s = 4.0
>>> test_square.area()
16.0

>>> tcircle = proto(r=1.61).chain(circle)
>>> tcircle.perimeter()
3.22

"""
