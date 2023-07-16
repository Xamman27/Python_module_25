from math import pi
class Circle:

    def __init__(self,x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def area_circle(self):
        return pi * self.radius ** 2

    def length(self):
        return 2 * pi * self.radius

