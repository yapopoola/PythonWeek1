from abc import ABC, abstractmethod
from math import pi, sqrt


class Shape(ABC):
    @abstractmethod
    def area(self): pass

    @abstractmethod
    def perimeter(self): pass

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return sqrt(max(s * (s - self.a) * (s - self.b) * (s - self.c), 0))

    def perimeter(self):
        return self.a + self.b + self.c

class Circle(Shape):
    def __init__(self, radius):
        self.radius = max(0, radius)

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = max(0, side)

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side
