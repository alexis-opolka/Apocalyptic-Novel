import random

class Item():
    def __init__(self, name, type="item", amount=1, max_actions=30, state="new"):
        self.name = name
        self.type = type
        self.price = random.randint(12, 100) if self.type == "clothing" else random.randint(25, 200)
        self.count = amount
        self.actions = max_actions
        self.initactions = max_actions
        self.state = state
        self.all = {
            "name": self.name,
            "type": self.type,
            "price": self.price,
            "count": self.count,
            "state": self.state,
            "available_actions": self.actions,
            "max_actions": self.initactions,
        }
        ### Out game attributes
        self.baseclass = self


class UsableItem(Item):
    def __init__(self, name, type="item", amount=1, max_actions=30, state="new"):
        ### Out game attributes
        self.baseclass = super
        super.__init__

    def Use(self):
        if self.actions > 0:
            self.actions -= 1
            print(f"{self.name} used 1 time")
            if self.actions == 0:
                print(f"{self.name} broke !")
                del self

    def Throw(self):
        print("You throw away {self.name} !")
        del self

    def Repair(self):
        self.actions = self.initactions

class Armor(Item):
    def __init__(self, name, durability):
        self.type = "armor"
        self.name = name
        self.durability = durability
        self.initdurability = durability
        self.state = random.choice(["used","new"])

        ### Out game attributes
        self.baseclass = super

class Weapon(Item):
    def __init__(self, name, durability, deg_pts, special_effect=None):
        self.name = name
        self.durability = durability
        self.deg_pts = deg_pts
        self.special_effect = special_effect

        ### Out game attributes
        self.baseclass = super

class ConsumableItem(Item):
    def __init__(self, name):
        self.name = name
