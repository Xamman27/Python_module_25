class Dot:
    count = 0

    def __init__(self, x, y):
        Dot.count += 1
        self.x = x
        self.y = y

    def print_info(self):
        print('x = {}\ny = {}\nCount = {}'.format(self.x, self.y, self.count))


first = Dot(0, 0)
second = Dot
first.print_info()

second = Dot(0, 0)
second.print_info()
