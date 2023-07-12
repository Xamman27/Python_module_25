import random
class Toyota:
    color = 'red'
    price = 1000000
    max_speed = 200
    speed_now = 0


car_1 = Toyota
car_2 = Toyota
car_3 = Toyota
car_list = [car_1, car_2, car_3]
for element in car_list:
    element.speed_now = random.randint(0, 200)
    print(element.speed_now)