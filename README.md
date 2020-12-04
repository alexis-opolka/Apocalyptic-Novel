Copyright (c) Unknown Games 2019-2020
# Zombie-Apocalypse
 Official code of Zombie Apocalypse

This repository contains a python version of what is developed by Centaurus.
It contains a version without the Ren'Py dependencies.
It's developed as modules and not as a part of the game itself.

Files and what it contains:

economy.py: TODO: system of dynamic marketplace using the value of the money, the demand and the storage.
            Faction, place, fame, karma, global state of the World can create variations on this system.
environment.py: It contains the World(), Environment(), Room() classes.
inventory.py: It contains the Inventory() class.
items.py: It contains the Item() class and some items for test purpose only.
labels.py: For now, it contains nothing.
lists.py: It contains some global lists used by nearly all the classes.
monsters.py: It contains the future Monsters classes.
player.py: It contains the base of the Player() class, need further research and dev.
pnjs.py: It contains the Pnj() class which is in active dev.
pnjs_nesfw_version.py: It contains an old-version of the one in pnjs.py with some NSFW method and aspects.
          It's about Sex, Kills and other aspects who can hurt the sensibility of persons.
renpy.py: It contains Ren'Py-only methods, used to have some Ren'Py code without having to add the Ren'Py package to the code.
taboo.py: It contains the system of taboos and the Taboo() class.


For any questions please contact us at unknowngamesoff@gmail.com
