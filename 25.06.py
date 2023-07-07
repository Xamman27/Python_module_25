class Dot:
    x = 0
    y = 0
    count = 0

    # def __init__(self, x, y):
    #     self.count += 1
    #     self.x = x
    #     self.y = y

    def print_info(self):
        print('x = {}\ny = {}\nCount = {}'.format(self.x, self.y, self.count))


first = Dot
second = Dot
first.print_info()
