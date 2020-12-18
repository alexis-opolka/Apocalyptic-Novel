import lists

class Faction:
    def __init__(self, name, ideologies, money, money_sign, territory_base, **kwargs):
        ### Strings
        self.name = name
        self.chief = None
        self.money = money
        self.money_sign = money_sign
        ### Numbers, int or float
        self.currency_value = 1 ### Currency value is 1 at default, can change in the future
        
        ### Lists
        self.ideologies = []
        self.territory = []
        self.members = []

        ### Dictionnaries
        self.relations = {}

        ### init process
        if type(ideologies) is list or type(ideologies) is tuple:
            for ideology in ideologies:
                self.ideologies.append(ideology)
        else:
            self.ideologies.append(ideologies)
        if type(territory_base) is list or type(territory_base) is tuple:
            for territory in territory_base:
                self.territory.append(territory)
        else:
            self.territory.append(territory_base)