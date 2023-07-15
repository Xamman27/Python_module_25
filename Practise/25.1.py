import random


class Warrior():

    def __init__(self, name):
        self.health = 100
        self.name = name

    def info_health(self):
        print(f"{self.name} have health is {self.health}")

    def damage(self, defender):
        if type(self) == type(defender):
            defender.health -= 20
        else:
           raise TypeError


scorpion = Warrior("Scorpion")
chan = Warrior("Chan")
while True:
    choose = int(input('Enter 1 for warriors attack each other\n''Enter 2 for exit from this battle: '))
    if choose == 1:
        offense = random.choice([scorpion, chan])
        defender = scorpion if offense == chan else chan
        offense.damage(defender)
        print(f'{offense.name} attack {defender.name}')
        defender.info_health()
        if defender.health == 0:
            print(f'{offense.name} is win')
            break
    elif choose == 2:
        break
    else:
        print('input error')

