# The Expression Problem


from protoclass import proto, clone


# We need some "legacy code" - data structures and functionality
# Data Structures


circle = proto(r=0.0)
triangle = proto(a=0.0, b=0.0, c=0.0)


# Functionality
def triangle_area(self):
    a, b, c = self.a, self.b, self.c
    s = (a + b + c) / 2.0
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5

triangle.area = triangle_area
circle.area = lambda self:\
    3.14159265359 * self.r ** 2.0


# New functionality
circle.perimeter = lambda self:\
    self.r * 2.0

triangle.perimeter = lambda self:\
    self.a + self.b + self.c


# New data structure and functionality
square = proto(s=0.0)
square.area = lambda self:\
    self.s * self.s

square.perimeter = lambda self:\
    self.s * 4.0


# We can test now

test_square = clone(square)
test_square.s = 4.0
print(test_square.area())

tcircle = proto(r=1.61).chain(circle)
print(tcircle.perimeter())

