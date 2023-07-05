class Family:
    name = 'common family'
    funds = 100000
    have_a_house = False


    def info(self):
        print(
            'Family name: {}\nFunds: {}\nFamily have a house: {}'.format(
                self.name, self.funds, self.have_a_house)
        )

family_1 = Family()
family_1.info()