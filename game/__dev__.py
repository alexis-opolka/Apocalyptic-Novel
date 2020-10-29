from taboo import *
from pnjs import Pnj
from player import Player
import monsters
import environment


### Vars
x = 0

### Objects
#### World, Environments and Rooms
root = environment.World()
#### Evironments
house = environment.Environment(root)
city = environment.Environment(root)
#### Rooms
bathroom = environment.Room(house, "Bathroom")
chamber = environment.Room(house, "Chamber")
kitchen = environment.Room(house, "Kitchen")

#### PNJs
master = Pnj(); master.RandomGender(); master.RandomName()
pnj = Pnj(); pnj.RandomName(); pnj.RandomTaboo()
pnj2 = Pnj("2")
pnj3 = Pnj("3")
pnj4 = Pnj("4")


pnj.EnterRoom(bathroom)
pnj2.EnterRoom(bathroom)
pnj3.EnterRoom(bathroom)
pnj4.EnterRoom(bathroom)


master.EnterRoom(bathroom)
master.AddTaboo(taboo_nude)
master.AddTaboo(taboo_nude)
master.BreakTaboo(taboo_nude)
master.SearchPeopleInRoom()
entry = input("Interact with: ")
for entity in master.can_interact:
    if entry == entity.name:
        master.InteractWith(entity)

print(master.thinks)
