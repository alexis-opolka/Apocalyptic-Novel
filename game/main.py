from datetime import datetime as dte
from taboo import *
from npc import NPC
from player import Player
import factions as fct
import monsters as mstr
import environment as env
import economy as eco
from items import (
    Item,
    UsableItem,
    Weapon,
    Armor)
import engine

################################################################################
###
###
### Objects initialzation
###
###
################################################################################
### Base of working of ZA
za = engine.Engine("Zombie Apocalypse", "0.2", "Unknown Games")
za.StartProcess()

### Simplifying the writing of Program-Classes
ZaList, ZaDict, ZaStr = engine.ZaList, engine.ZaDict, engine.ZaStr
engine_list = ZaList(["test_list_element", "test_list_element_2"])
engine_dict = ZaDict("test_key", "test_value")
engine_str = ZaStr("test_string")


### World, Environments and Rooms
root = env.World()

### Evironments
house = env.Environment(root)
city = env.Environment(root)
### Rooms
bathroom = env.Room(house, "Bathroom")
chamber = env.Room(house, "Chamber")
kitchen = env.Room(house, "Kitchen")

### NPCs
master = NPC()
chief_1 = NPC("Maximilian")
pnj = NPC()
pnj2 = NPC("2")
pnj3 = NPC("3")
pnj4 = NPC("4")

### Player
mp = Player("Centaurus", 21)

### Factions
shagards = fct.Faction(root, "Shagards", ("Anarchisme"), "Shouraves", "$", ("A1", "A1"))
romans = fct.Faction(root, "Romains", ("Suprématie"), "Triens", "T", ("A1", "B1"))


### MarketPlaces
Global = eco.GlobalMarketPlace(root)

### Items
dress = Item("Dress", "clothing", 5, 40)
dress_used = Item("Dress", "clothing", 5, 40, "used")
collar = Item("Collar", "jewelry", 3, 7)
collar_used = Item("Collar", "jewelry", 3, 40, "used")
bag_eastpak = Item("Eastpack Bag", "bag", 2, "unlimited")
knife = Weapon("Knife", "weapon", 1, 50)
ak47 = Weapon("AK47", "fire_weapon", 1, 90)
jacket = UsableItem("Jacket", "clothing", 8, 60)
pen = Item("Pen", "tool", 20, 20)
plastron = Armor("Plastron", 40)



### Program-wide global variables








################################################################################
###
###
### Actions on objects
###
###
################################################################################

master.RandomGender(); master.RandomName()
pnj.RandomName(); pnj.RandomTaboo()
#mp.SayStats()






################################################################################
###
###
### Debugging statements
###
###
################################################################################
print(engine_dict, engine_list, engine_str)
#print(items_list)
#print(globals())
open("_debug-info.txt", "w").write(za.DictToStr(za.StoreObjectAttributesDict(master)))

za.EndProcess()





print(f"{za.title} - {za.version} finished at: {dte.now()}\n\n")

#en gros pour chaque acteur j'ai une variable qui représente
# sa demande (de 0 à 1000 mais ça pourrait aller de +inf à -inf)
#plus une constante qui dit de combien sa demande augmente par jour
#pour avoir un prix fixé entre 1 et 100 (que tu peux voir comme un
# pourcentage du prix maximal que l'acteur est prêt à payer) j'ai
# une formule à base de cotangente
#int(50+math.atan(float(need)/float(conso))*100/math.pi),
# need et conso sont les deux variables ci-dessus
#tu peux retirer le int si tu veux un prix flottant mais je trouve pas
# ça super réaliste
#et à chaque fois que tu vend (ici de l'épice),
# tu retranches la quantité vendue (ou une valeur qui y est proportionnelle)
# à son need (la valeur entre 0 et 1000),
# et tu t'ajoutes prix x quantité d'argent

### Tests Functions
def StoreObjectPropertiesDict(object):
    Properties = {p:getattr(object, p) for p in dir(object) if isinstance(getattr(object, p), (int, float, str, list, dict))}
    return Properties
