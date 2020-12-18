from main import *


### Vars
x = 0


### Actions
pnj.EnterRoom(bathroom)
pnj2.EnterRoom(bathroom)
pnj3.EnterRoom(bathroom)
pnj4.EnterRoom(bathroom)


master.EnterRoom(bathroom)
master.AddTaboo(taboo_nude)
master.AddTaboo(taboo_nude)
master.BreakTaboo(taboo_nude)
master.SearchPeopleInRoom()
entry = pnj.name
for entity in master.can_interact:
    if entry == entity.name or entry == entity:
        master.InteractWith(entity)


master.JoinFaction(Shagards)
