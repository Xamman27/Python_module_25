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

    def find_cross(self,circle_2):
        distance = ((self.x - circle_2.x) ** 2 + (self.y - circle_2.y) ** 2) ** 0.5
        if distance > self.radius + circle_2.radius:
            print('Do not intersect')
        elif distance < ((self.radius - circle_2.radius) ** 2) ** 0.5:
            print('Do not intersect, one circle inside other')
        else:
            print('Intersect')

    def increase(self, factor):
        self.radius = self.radius * factor


a = Circle(0, 0, 1)
b = Circle(2, 2, 2)
a.find_cross(b)
b.increase(10)
a.find_cross(b)