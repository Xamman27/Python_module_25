class Toyota:
    current_speed = 0


    def __init__(self, color, price, max_speed):
        self.color = color
        self.price = price
        self.max_speed = max_speed


    def print_info(self):
        print('Color is{}\nPrice is {}\nMaximal speed is {}\nCurrent speed is {}'.format(
            self.color, self.price, self.max_speed, self.current_speed))


    def set_speed(self,speed):
        self.current_speed = speed

my_car = Toyota('Red', 100, 230)
my_car.print_info()
my_car.set_speed(120)
my_car.print_info()



