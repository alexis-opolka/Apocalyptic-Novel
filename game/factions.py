import lists
import random

class Faction:
    def __init__(self, world, name, ideologies, money, money_sign, territory_base=None, **kwargs):
        self.root = world
        ### Strings
        self.name = name
        self.chief = None
        self.money = money
        self.money_sign = money_sign
        ### Numbers, int or float
        self.currency_value = 1 ### Currency value is 1 at default, can change in the future

        ### Lists
        self.ideologies = []
        self.members = []
        self.territory = []

        ### Dictionnaries
        self.relations = {}


    ### Relations-only methods
    def Encounters(self, faction, log=False):
        if not faction in self.relations:
            self.relations[faction] = "neutral"
            faction.relations[self] = "neutral"
            if log == True:
                print(self.name, "encountered", faction.name)

    def DeclaresWar(self, faction, log=False):
        if self.relations[faction] != "ennemy":
            if log == True:
                print(self.name, "declared war to", faction.name)
            self.relations[faction] = "ennemy"
            faction.relations[self] = "ennemy"


    ### Map-related methods
    def OwnLand(self, cell_name, log=False):
        if cell_name in self.root.map:
            if cell_name not in self.territory:
                if self.root.map[cell_name]["owner"] is not None:
                    print("This cell has already an owner and can't be owned by another faction")
                else:
                    self.root.map[cell_name]["owner"] = self
                    self.territory.append(cell_name) ###TODO: Create a pointer to Dictionary element
                    if log == True:
                        print(self.name, "owns", cell_name)
            else:
                print("You already own this cell so can't be owned again")

    def AttackLand(self, from_troops_cell, to_troops_cell, troops_amount, log=False):
        if self.root.map[to_troops_cell]["troops"] != 0:
            r = self.AttackTroops(self.root.map[to_troops_cell]["troops"], troops_amount)
            if r[0] is False:
                self.root.map[from_troops_cell]["troops"] -= r[1]
                self.root.map[to_troops_cell]["troops"] = r[2]
                if log is True:
                    print("Attack failed at", to_troops_cell)
            else:
                self.root.map[from_troops_cell]["troops"] -= troops_amount
                self.root.map[to_troops_cell]["troops"] = r[1]
                if log is True:
                    print("Attack succeed at", to_troops_cell)
                self.ConquerLand(to_troops_cell, True)
            print(self.root.map[from_troops_cell]["troops"], self.root.map[to_troops_cell]["troops"])
        else:
            print("We can't attack this cell:", from_troops_cell)

    def ConquerLand(self, cell_name, log=False):
        if cell_name in self.root.map:
            if cell_name not in self.territory:
                if self.root.map[cell_name]["troops"] == 0:
                    self.root.map[cell_name]["owner"] = self
                    self.root.map[cell_name]["status"] = "in transition"
                    if log == True:
                        print(self.name, "conquered", cell_name)
            else:
                print("You can't conquer a cell you already own")

    #### Non-Player methods
    def GetCellStats(self, cell_name):
        if cell_name in self.territory:
            return self.root.map[cell_name]

    def GetCellStatsHistory(self, cell_name):
        if cell_name in self.territory:
            return self.root.map[cell_name]


    ### Troops-Related methods
    def RecruitTroops(self, cell_name, amount, log=False):
        if cell_name in self.root.map:
            self.root.map[cell_name]["troops"] += amount
            if log is True:
                print(self.name, "recruited", amount, "troops in", cell_name)

    def MoveTroops(self, from_cell_name, to_cell_name, amount):
        if from_cell_name in self.root.map:
            if from_cell_name in self.territory:
                if self.root.map[from_cell_name]["troops"] >= amount:
                    pass
                else:
                    print("Can't move more troops than you have on a cell")
                    return
            else:
                print("Can't move troops from a cell wich isn't owned by us")
        else:
            print("The cell isn't in the map")
        if to_cell_name in self.root.map:
            if to_cell_name in self.territory:
                self.TransferTroops(from_cell_name, to_cell_name, amount, True)
            if to_cell_name not in self.territory and to_cell_name in self.root.map:
                if self.relations[self.root.map[to_cell_name]["owner"]] == "ennemy":
                    ans = input("Do you really want to attack? [Y,N] ")
                    if ans.lower() in ["y", "yes"]:
                        self.AttackLand(from_cell_name, to_cell_name, amount, True)
                if self.relations[self.root.map[to_cell_name]["owner"]] == "ally":
                    ans = input("Do you really want to Transfer troops? [Y,N] ")
                    if ans.lower() in ["y", "yes"]:
                        self.TransferTroops(from_cell_name, to_cell_name, amount, True)
                else:
                    if self.root.map[to_cell_name]["owner"] != None:
                        if self.root.map[to_cell_name]["owner"] in self.relations:
                            if self.relations[self.root.map[to_cell_name]["owner"]] == "neutral":
                                print("We can't do anything with a territory from a neutral acquaintance")
                        else:
                            print("This cell is owned by an unkown faction")
                    else:
                        self.TransferTroops(from_cell_name, to_cell_name, amount, True)

    def TransferTroops(self, from_troops_cell, to_troops_cell, troops_amount, log=False):
        self.root.map[from_troops_cell]["troops"] -= troops_amount
        self.root.map[to_troops_cell]["troops"] += troops_amount
        if log == True:
            print(self.name, "transferred", troops_amount, "from", from_troops_cell, "to", to_troops_cell)

    def AttackTroops(self, defenders_amount, attackers_amount):
        r = None
        print(r, attackers_amount, defenders_amount)
        if attackers_amount > defenders_amount:
            r = True
            if attackers_amount > (2*defenders_amount):
                defenders_amount = 0
                attackers_amount -= round(defenders_amount/2)
            else:
                attackers_amount -= defenders_amount
                defenders_amount = 0
        elif attackers_amount == defenders_amount:
            luck = random.choice([True, False])
            if luck is False:
                r = False
                attackers_amount = 0
                defenders_amount -= random.randrange(0, defenders_amount-1)
            else:
                r = True
                attackers_amount -= random.randrange(0, attackers_amount-1)
                defenders_amount = 0
        else:
            r = False
            attackers_amount -= random.randrange(1, attackers_amount)
            defenders_amount -= random.randrange(0, attackers_amount)
        print(r, attackers_amount, defenders_amount)
        return (r, attackers_amount, defenders_amount)
