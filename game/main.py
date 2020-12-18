from taboo import *
from npc import NPC
#from player import Player
import factions as fct
import monsters as mstr
import environment as env
import economy as eco

### Objects
#### World, Environments and Rooms
root = env.World()
#### Evironments
house = env.Environment(root)
city = env.Environment(root)
#### Rooms
bathroom = env.Room(house, "Bathroom")
chamber = env.Room(house, "Chamber")
kitchen = env.Room(house, "Kitchen")

#### PNJs
master = NPC(); master.RandomGender(); master.RandomName()
chief_1 = NPC("Maximilian")
pnj = NPC(); pnj.RandomName(); pnj.RandomTaboo()
pnj2 = NPC("2")
pnj3 = NPC("3")
pnj4 = NPC("4")


#### Factions
Shagards = fct.Faction("Shagards", ("Anarchisme"), "Shouraves", "$", ("Sud_1", "Sud_2"))


#### MarketPlaces
Global = eco.GlobalMarketPlace()


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