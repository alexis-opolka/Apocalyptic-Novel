from lists import *

class Faction:
    def __init__(self, name, ideologies, chief, money, money_sign, territory_base, **kwargs):
        self.name = name
        self.chief = chief
        self.money = money
        self.money_sign = money_sign
        self.ideologies = ideologies
        self.territory = territory_base
