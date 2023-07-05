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


    def buy_house(self):

family_1 = Family()
family_1.info()
family_1.add_money(10)
family_1.info()
