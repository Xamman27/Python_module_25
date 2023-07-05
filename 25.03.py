class Toyota:
    color = 'red'
    price = 1000000
    max_speed = 200
    speed_now = 0

    def car_info(self):
        print(
            'color: {}\nprice: {}\nmax speed: {}\nspeed now: {}'.format(
                self.color, self.price, self.max_speed, self.speed_now))

    def add_speed_now(self, speed):
        self.speed_now = speed

car_1 = Toyota

car_1.add_speed_now(car_1, 100)
car_1.car_info(car_1)
