import random
class Warrior:
    def __init__(self, name):
        self.health = 100
        self.name = name

    def info_health(self):
        print("{}have health is {}".format(self.name, self.health))

    def damage(self, defender):
        if type(self) == type(defender):
            defender.health -= 20
        else:
           raise TypeError


players = []
player_1 = Warrior("Scorpion")
player_2 = Warrior("chan")

players.append(player_1)
players.append(player_2)

while True:
    choose = int(input('Enter 1 for warriors attack each other\n'
                   'Enter 2 for exit from this battle: '))
    if choose == 1:
        randon_num = random.randint(0, 1)
        players[0].info_health()
        players[1].info_health()
        players[randon_num].damage(players[randon_num - 1])
        print(
            f'{players[randon_num].name} attacks {players[randon_num - 1].name}\n Healths {players[randon_num - 1].name}'
            f' is {players[randon_num - 1].info_health}')
        if players[randon_num - 1].health == 0:
            print(players[randon_num].name,' is win')
            break
    elif choose == 2:
        break
    else:
        print('input error')

