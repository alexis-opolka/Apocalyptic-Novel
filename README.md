# Apocalyptic-Novel

## Official code of Apocalyptic Novel

    This repository contains a python version of what is developed by Centaurus.
    It contains a version without the Ren'Py dependencies.
    It's developed as modules and not as a part of the game itself.

## Files and what it contains

### economy.py

    TODO: system of dynamic marketplace using the value of the money, the demand and the storage.
    Faction, place, fame, karma, global state of the World can create variations on this system.

    Started to work on the system and done some achievements but still not much to be called progress.

### engine.py

    A file containing the game engine of the game, it handles all the methods for doing work on the client and is used to render windows with our game engine.
    Contains both engine the visual and physical one.

### environment.py

    It contains the World(), Environment(), Room() classes.
    Pyramidal architecture of game environment but still is the base of the front-end of the game.
    Still needs further work in the future.

### inventory.py

    It contains the Inventory() class.
    Not much to say than it's maybe going to be modified for having further features and abilities.

### items.py

    It contains the Item() class.
    It will be modified after the NPC class.

### labels.py

    For now, it contains nothing.
    It will contains an class made to improve the  creation of labels and change their behaviour.

### lists.py

    It contains some global lists used by nearly all the classes.
    This file will be deprecated in the near future, we transfer the variables stored inside wether in engine.py or in files where they're truly used at their most potential.

### monsters.py

    It contains the future Monsters classes. Still not developed yet, see roadmap.md for further informations.

### player.py

    It contains the base of the Player() class, need further research and dev. Will be worked on in the future.

### npc.py

    It contains the Npc() class which holds for now 5 classes, in the near future the class will be updated and enhanced with optimisations made.

### pnjs_nsfw_version.py

    Deprecated version of old file pnjs.py, contains multiple ideas about NSFW content.
    Will be removed in the future when the corrections of NPC() class will be done.

### renpy.py

    It contains Ren'Py-only methods, used to have some Ren'Py code without having to add the Ren'Py package to the code.
    It will contains an API-like class in the future for handling commands with the Ren'Py game engine.

### taboo.py

    It contains the system of taboos and the Taboo() class.

### For any questions please contact us at unknowngamesoff@gmail.com

#### Copyright (c) Unknown Games 2019-2021
