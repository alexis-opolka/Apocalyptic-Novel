class Inventory():
    def __init__(self):
        self.content = {}

    def Contains(self, item): ### We verify if we have the item in the inventory
        if item.name in self.content:
            if self.content[item.name]["count"] >= 1:
                return True
            else:
                return False
        else:
            return False

    def Remove(self, item): ### We remove an item in the inventory
        if self.Contains(item):
            self.content[item.name]["count"] -= 1
            if self.content[item.name]["count"] <= 0:
                del self.content[item.name]

    def Add(self, item): ### We add an item in the inventory
        if item.name in self.content:
            self.content[item.name]["count"] += 1
        else:
            if item.count > 0: ### We check if the amount of items in Item() object is greater than zero
                self.content.update({ ### If true: we add the item in the inventory for the first time
                    item.name: {
                        "count": 1,
                        "base-object": item
                    }
                })
                item.count -= 1 ### As we grabbed one item in the Item() object we remove 1 in the count

    def ListEverything(self):
        for key, value in self.content.items():
            print(f" {key} : {value['base-object'].all}")
