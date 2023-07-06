class Family:
    name = 'common family'
    funds = 100000
    have_a_house = False


    def info(self):
        print(
            'Family name: {}\nFunds: {}\nFamily have a house: {}'.format(
                self.name, self.funds, self.have_a_house)
        )

    def add_money(self, summ):
        Family.funds += summ


    def buy_house(self, house_price, discount):
        if self.funds >= house_price - house_price * discount / 100:
            self.have_a_house = True
            self.funds -= house_price - house_price * discount / 100
            print('Congrats {}\nYou buy  house\nYou funds now {}'.format(self.name,self.funds))
        else:
            print('Not enough money\nWork more')


family_1 = Family()
family_1.info()
family_1.add_money(100)
family_1.info()
family_1.buy_house(100000, 10)