import random

class Item():
    def __init__(self, name, type="item", amount=1, actionsmax=30, state="new"):
        self.name = name
        self.type = type
        self.price = random.randint(12, 100) if self.type == "clothing" else random.randint(25, 200)
        self.count = amount
        self.actions = actionsmax
        self.initactions = actionsmax
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

    class Armor():
        def __init__(self, name, durability):
            self.type = "armor"
            self.name = name
            self.durability = durability
            self.initdurability = durability
            self.state = random.choice(["used","new"])


###########################################################
### We define some items
###########################################################
dress = Item("Dress", "clothing", 5, 40)
dress_used = Item("Dress", "clothing", 5, 40, "used")
collar = Item("Collar", "jewelry", 3, 7)
collar_used = Item("Collar", "jewelry", 3, 40, "used")
bag_eastpak = Item("Eastpack Bag", "bag", 2, "unlimited")
knife = Item("Knife", "weapon", 1, 50)
ak47 = Item("AK47", "fire_weapon", 1, 90)
jacket = Item("Jacket", "clothing", 8, 60)
pen = Item("Pen", "tool", 20, 20)

plastron = Item.Armor("Plastron", 40)
