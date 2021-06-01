from datetime import datetime as dte
from taboo import Taboo
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
### Objects initialAntion
###
###
################################################################################
### Base of working of An
an_engine = engine.Engine("Apocalyptic Novel", "0.2", "Unknown Games")


### Simplifying the writing of Program-Classes
AnList, AnDict, AnStr = engine.AnList, engine.AnDict, engine.AnStr
engine_list = AnList(["test_list_element", "test_list_element_2"])
engine_dict = AnDict("test_key", "test_value")
engine_str = AnStr("test_string")


### World, Environments and Rooms
root = env.World()

### Evironments
house = env.Environment(root)
city = env.Environment(root)
### Rooms
bathroom = env.Room(house, "Bathroom")
chamber = env.Room(house, "Chamber")
kitchen = env.Room(house, "Kitchen")

### Taboo system
taboo_list = []
#### We initialize the taboos & executed the minimal settings
Taboo.setGlobalList(taboo_list)
taboo_nude = Taboo("Nudity")
taboo_wear = Taboo("Wearing")
taboo_nude.setContrary(taboo_wear)

taboo_sex = Taboo("Sex")
taboo_nosex = Taboo("No Sex")
taboo_sex.setContrary(taboo_nosex)

taboo_bj = Taboo("Blowjob")
taboo_nobj = Taboo("No Blowjob")
taboo_bj.setContrary(taboo_nobj)

taboo_kill = Taboo("Killing")
taboo_save = Taboo("Saving")
taboo_kill.setContrary(taboo_save)

taboo_egality = Taboo("Equality")
taboo_slavery = Taboo("Slavery")
taboo_egality.setContrary(taboo_slavery)

taboo_capitalism = Taboo("Capitalism")
taboo_socialism = Taboo("Socialism")
taboo_capitalism.setContrary(taboo_socialism)

taboo_test = Taboo("test")

### NPCs
NPC.setTabooList(taboo_list)

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
an_engine.StartQtProcess(maximized=True)
#print(engine_dict, engine_list, engine_str)
#print(items_list)
#print(globals())
open("_debug-info.txt", "w").write(an_engine.DictToStr(an_engine.StoreObjectAttributesDict(master)))
#print(NPC.taboo_list)
an_engine.EndProcess()

print(f"{an_engine.title} - {an_engine.version} finished at: {dte.now()}\n\n")

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
