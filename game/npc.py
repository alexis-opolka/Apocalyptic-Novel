from lists import TabooList
from renpy import renpy
import random
import inventory
import environment

"""
    This module contains the entire class for the NPC, no more no less.
"""



class NPC: #TODO: Change __init__ to have less dependencies
    """
        This class is only used for NPC.
        We alternate the Point of View(POV) for the actions and sometimes have the two pov available for
        actions.
        For having the best reusability in no time, we mainly use the random module.

        Dependencies:\n
            - random module
            - lists module
            - inventory module
    """
    ### Class global list
    #### Names
    male_names_list = ["Georges", "Mathieu", "Michael", "Nicolas", "Yohann"]
    fem_names_list = ["Millie","Camille", "Jade", "Marine", "Andréa", "Lily"]
    #### Body
    hair_color_list = ["brown", "black", "blond", "ginger"]
    haircut_list = ["short", "medium", "long"]
    hair_styles_list =  [""]
    eyes_color_list = ["grey", "blue", "yellow", "green", "red", "brown"]
    skin_color_list = ["white", "asian", "black"]
    facial_pilosity_list = ["little", "average", "big"]
    breast_size_list = ["little", "average", "big"]
    ass_size_list = ["little", "average", "big"]
    status_list = ["normal", "pregnant"]
    #### City
    city_list = ["Paris", "Béziers", "London", "Berlin", "New York", "Los Angeles", "San Francisco"]
    #### Replies
    reply_list = ("What ?", "I have nothing to say to you!", "What again ?!")
    #### Booleans
    bool_list = (True, False)
    ### predefined global NPC attributes
    taboo_list = None

    def setTabooList(list):
        NPC.taboo_list = list


    def __init__(
        self,
        name="?",
        colour="#f9300c",
        sex="fem",
        min_age=17,
        max_age=36,
        is_enslaved=False,
        profile_image="images/pnj.png",
        font="Avara.tff",
        dialogue_colour="#ffffff"):

        self.taboo_list = NPC.taboo_list
        ### Strings Creator-defined
        self.c = renpy.Character(name, # The name to be displayed above the dialogue.
            what_font = font, # The font to be used for the character.
            who_font = font,
            color = colour, # The colour of the character's NAME section
            what_color = dialogue_colour) # The colour of the character's dialogue.
        self.age = random.randint(min_age, max_age) # Aged Randomly defined between min and max age given when __init__() called
        self.name = name # Used to have the name of Object and NPC
        self.color = colour # Theoric use: Add it in the Character() function for having the NPC have this color
        self.sex = sex # Used to know the genre of NPC and conjugate phrases to male or female prefix
        self.profile_image = profile_image # used to show the image when NPC talks
        ## TODO: self.genre --> self.sex, make appropriate modifications
        if self.sex == "fem":
            self.sex_name = "Woman" # Name used to properly define NPC's genre, here it's a female
        elif self.sex == "man":
            self.sex_name = "Man" # Name used to properly define NPC's genre, here it's a male
        else:
            self.sex_name = "Undefined" # Name used to properly define NPC's genre, here it's not given or NPC is non binary
        self.status = NPC.status_list[0]

        ### Strings Randomly defined
        self.hair_color = random.choice(NPC.hair_color_list) # Store the hair color, after used to show layered images
        self.eyes_color = random.choice(NPC.eyes_color_list) # Store the eyes color, after used to show layered images
        self.born_city = random.choice(NPC.city_list) # Store the city of born, after used to change value of price when enslaved

        ### Numbers: int/float | int preferred
        self.life = 100 # Life of npc | It's used for doing things who needs life to be sure to be able to come back
        self.trust = 0 # Trust of npc to someone | It's used to gain npc in the team of Player
        self.suspicion = 0 # Suspicion of npc to someone | It's used to determine the probability of doing smthng
        self.love = 0 # Love of npc to someone
        self.anger = 0 # Anger of npc to someone
        self.fear = 0 # Fear of npc of someone or a group | Person is preferred
        self.corr = 0 # Corruption of npc | Help to do illegal things with him
        self.loyalty = 0 # Loyalty of npc to a camp, ideology or person
        self.inf = 30 # Infuence of npc
        self.price = random.randint(150, 10000) # Price of npc when he's enslaved, if not set manually
        self.money = 0 # Money the npc have, currently 0
        self.will = random.randint(20, 100) # Will of npc to do an action and the ability to be influenced or not | Can be broken with training if enslaved or can be upgraded with actions
        self.obedience = 0 # Obedience of npc | Only used when self.enslaved is True
        self.shame = 100 # Shame of npc | only used when self.enslave is True
        self.karma = 0 # Karma of npc | Used to determine if can do bad or good things
        self.happiness = 100 # Happiness of npc | Used to determine if is in depression or not

        ### Booleans
        if is_enslaved == True:
            self.enslaved = True # npc is a slave | Only used to know enslavement
            self.free = False # npc is not free | Used to know certain amount of things: slavery, faction, prisoner, etc...
        elif is_enslaved == False:
            self.enslaved = False # npc isn't a slave | Only used to know enslavement
            self.free = True # npc is free | Used to know certain amount of things: slavery, faction, prisoner, etc...
        self.dead = False # npc is dead
        self.suicided = False # npc suicided
        self.killed = False # npc has been killed
        self.kidnapped = False # npc has been kidnapped
        self.virgin = False # if False npc is a virgin otherwise he's not and the value is True

        ### None defined properties
        self.owner = None # Used to store object reference of Owner | Only used when npc is enslaved, self.enslaved == True
        self.inroom = None # Used to store object reference of the Room
        self.interacts = None # Used to store object of the current npc/Player the npc is interacting with

        ### Lists
        self.knows = [] # npc/Player is added when npc hears of him/her
        self.encounters = [] # npc/Player is added when npc speaks to them for the first time
        # Every relationships of npc
        self.relationships = []
        self.can_interact = [] # List of npc/Player with whom the npc can interact, it's cleared when we quit the room | Used to dynamically interact with the npcs of the Room
        self.slaves = [] # Every slaves of npc
        self.joined = []

        ### Dictionnaries
        self.inventory = inventory.Inventory() # Inventory of npc | property is in fact an object of class Inventory()
        self.thinks = {} ### Under Development: Dictionnary made to know the attributes given to each aquaintance
        self.taboos = {} # Here are placed the taboos of npc as [Taboo-object, [If has, Broken Index,Player knows]]
        self.records = {} ### TODO: Develop a system to store the differents records of action | used to make statistics

        ### We call methods to set some base-properties
        self.SetTaboo()

        ### Out game attributes
        self.baseclass = NPC

    ######################################################
    ####    We have an impact on Vars of npc's
    ######################################################

    def SetMoney(self, money):
        self.money = money

    def GetAge(self):
        return self.age
    def GetName(self):
        return self.name

    def IsHurted(self, hp):
        self.life -= hp
        print("Ouch!")
    def IsHealing(self, hp):
        self.life += hp
        print("Ahh! It's better!")

    def AddSuspicion(self, amount):
        if self.interacts != None:
            self.thinks[self.interacts]["suspicion"] += amount
    def SustSuspicion(self, amount):
        if self.interacts != None:
            self.thinks[self.interacts]["suspicion"] -= amount

    def AddLove(self, amount):
        if self.interacts != None:
            self.thinks[self.interacts]["love"] += amount
    def SustLove(self, amount):
        if self.interacts != None:
            self.thinks[self.interacts]["love"] -= amount

    def AddAnger(self, amount):
        if self.interacts != None:
            self.thinks[self.interacts]["anger"] += amount
    def SustAnger(self, amount):
        if self.interacts != None:
            self.thinks[self.interacts]["anger"] -= amount

    def AddFear(self, amount):
        if self.interacts != None:
            self.thinks[self.interacts]["fear"] += amount
    def SustFear(self, amount):
        if self.interacts != None:
            self.thinks[self.interacts]["fear"] -= amount

    def AddCorruption(self, amount):
        if self.interacts != None:
            self.thinks[self.interacts]["corruption"] += amount
    def SustCorruption(self, amount):
        if self.interacts != None:
            self.thinks[self.interacts]["corruption"] -= amount

    def AddLoyalty(self, amount):
        if self.interacts != None:
            self.thinks[self.interacts]["loyalty"] += amount
    def SustLoyalty(self, amount):
        if self.interacts != None:
            self.thinks[self.interacts]["loyalty"] -= amount

    def SetInfluence(self, amount):
        self.inf = amount

    def Suicide(self):
        self.dead = True
        self.suicided = True

    def HaveSex(self, *names):
        self.virgin = True
        self.relationships.append(names)

    #############################################################
    #### We print Information Or It's actions including speaking
    #############################################################
    def SayStats(self):
        if not self.enslaved:
            print("\nI'm a "+self.sex_name+".")
            print("My life is at "+str(self.life)+" hp, I have "+str(self.suspicion)+" suspicion points.")
            print("I have "+str(self.love)+" love points, I'm pissed off at "+str(self.angry)+" points")
            print("I'm feared at "+str(self.fear)+" points. I'm corrupted at "+str(self.corr)+" points")
            print("My loyalty is at "+str(self.loyalty)+" points, I have "+str(self.inf)+" influence points")
            print("If I'm enslaved, my price is "+str(self.price)+" $")
            print("I have "+str(self.money)+" $ in my wallet")
            if self.enslaved == False and self.free == True: print("Hopefully for me I'm not enslaved")
            else: print("And... I'm enslaved")

            if self.dead == False: print("Hey I'm alive!")
            else: print("Hey I'm dead! (I know)")

            if self.suicided == False: print("I haven't commit suicide")
            else: print("I suicided myself....")

            if self.killed == False: print("No one killed me")
            else: print("Someone killed me")

            if self.kidnapped == False: print("No one kidnapped me!")
            else: print("Someone kidnapped me!")

            if self.virgin == False: print("I haven't had a relation with someone!")
            else: print("I had a relation with someone wouhou!")
        else:
            print("...")

    def SayMyRelations(self):
        if not self.enslaved:
            if self.relationships is None:
                print("I haven't had a relation with someone...")
            else:
                print(self.name,"I had relations with"+str(self.relationships))
        else:
            print("...")

    def talk(self):
        if not self.enslaved:
            print(random.choice(NPC.reply_list))
        else:
            print("...")
    def cry(self):
        if not self.enslaved:
            print("What do you want ??? sniff sniff")
        else:
            print("...")
    def Presents(self):
        if not self.enslaved:
            print("My name is "+self.name+" and I'm "+str(self.age)+" yo...")
            print("I have "+self.hair_color+" hairs and "+self.eyes_color+" eyes")
            print("I'm born in "+self.born_city)
        else:
            print("Ask to my", "master" if self.owner.genre == "man" else "mistress", "for more informations...")

    #################################################
    ### Actions using labels and screens
    #################################################
    def CallLabel(self, label):
        renpy.call(label)

    #################################################
    ### Actions using images
    #################################################
    def ShowAt(self, position):
        renpy.show(self.profile_image)

    #################################################
    ### Randomization of Vars
    #################################################
    def RandomName(self):
        if self.sex == "fem":
            self.name = random.choice(NPC.fem_names_list)
        elif self.sex == "man":
            self.name = random.choice(NPC.male_names_list)
        else:
            print("Genre is not properly defined")

    def RandomGender(self):
        self.genre = random.choice(["man", "fem"])

    def RandomMoney(self):
        self.money += random.randint(0, 8000)



    def RandomInfluence(self):
        self.inf += random.randint(0, 100)

    def RandomEnslavement(self):
        self.enslaved = random.choice(NPC.bool_list)
        if self.enslaved == True:
            self.GetEnslaved()
        else:
            self.free = True

    def RandomInventory(self, items_list):
        x = random.randint(1, items_list)
        while x > 0:
            self.inventory.Add(random.choice(items_list))
            x -= 1

    ##################################################
    ### Inventory-Related Methods
    ##################################################
    def OpenInventory(self):
        if not self.enslaved:
            for key, value in self.inventory.content.items():
                print(key, ":", value["base-object"])
        else:
            print("As a slave, I don't have any possession...")
    def ShowInventory(self):
        if not self.enslaved:
            for key, value in self.inventory.content.items():
                print(key, ":", value)
        else:
            print("As a slave I don't have any possessions...")

    def MergeInventory(self, receiver):
        for key, item in self.inventory.content.items():
            receiver.inventory.Add(item["base-object"])

    ##################################################
    ### Slave-Related Methods
    ##################################################
    def SetSlavePrice(self, slave, price):
        if not self.enslaved:
            slave.price = price
        else:
            print("I'm a slave and can't do anything if my master haven't ordered it to me...")

    def GetEnslaved(self, owner): # pov of slave | npc is forced to
        if not self.enslaved:
            self.enslaved = True
            self.free = False
            owner.slaves.append(self)
            self.owner = owner
            self.InventoryMerge(owner)
        else:
            print(f"{self.name} is already enslaved, we can't enslave someone twice!")
    def Enslave(self, slave): # pov of owner | npc force someone
        if not slave.enslaved:
            slave.enslaved = True
            self.free = False
            self.slaves.append(slave)
            slave.owner = self
            slave.InventoryMerge(self)
        else:
            print(f"{slave.name} is already enslaved, we can't enslave someone twice!")

    def PresentSlave(self): # pov of owner
        if not len(self.slaves) == 0:
            print(f"I have {len(self.slaves)}", " slave" if len(self.slaves) == 1 else "slaves")
            if len(self.slaves) == 1:
                print("His" if self.slaves[0].genre == "man" else "Her", f"name is {self.slaves[0].name}")
            else:
                print("Their name are:")
                for slave in self.slaves:
                    print(f"- {slave.name}")
        else:
            print("I don't have any slaves")
        print("")
    def PresentOwner(self): # pov of slave
        print("I'm the slave of", self.owner.name)
        print("Ask to","him" if self.owner.genre=="man" else "her", "for more informations...", end="\n\n")

    def Train(self, slave): # pov of owner/master
        if not self.enslaved:
            if slave in self.slaves:
                if slave.obedience <= 25:
                    training = random.randint(1, 8)
                    if training < 4:
                        ObedienceToAdd = random.randint(1 , 5)
                        print("The training goes bad...")
                    elif training > 4 and training < 8:
                        ObedienceToAdd = random.randint(3, 7)
                        print("The training goes well.")
                    else:
                        ObedienceToAdd = random.randint(5, 8)
                        print("The training goes perfectly well")
                elif slave.obedience > 25 and slave.obedience <= 50:
                    training = random.randint(2, 9)
                    if training < 4:
                        ObedienceToAdd = random.randint(1 , 6)
                        print("The training goes bad...")
                    elif training > 4 and training < 8:
                        ObedienceToAdd = random.randint(3, 7)
                        print("The training goes well.")
                    else:
                        ObedienceToAdd = random.randint(5, 8)
                        print("The training goes perfectly well")
                elif slave.obedience > 50 and slave.obedience <= 75:
                    training = random.randint(2, 10)
                    if training < 4:
                        ObedienceToAdd = random.randint(1 , 7)
                        print("The training goes bad...")
                    elif training > 4 and training < 8:
                        ObedienceToAdd = random.randint(3, 8)
                        print("The training goes well.")
                    else:
                        ObedienceToAdd = random.randint(5, 9)
                        print("The training goes perfectly well")
                else:
                    training = random.randint(3 ,12)
                    if training < 4:
                        ObedienceToAdd = random.randint(1 , 8)
                        print("The training goes bad...")
                    elif training > 4 and training < 8:
                        ObedienceToAdd = random.randint(3, 9)
                        print("The training goes well.")
                    else:
                        ObedienceToAdd = random.randint(5, 10)
                        print("The training goes perfectly well")
                if slave.obedience+ObedienceToAdd > 100:
                    slave.obedience = 100
                else:
                    slave.obedience += ObedienceToAdd
                print(f"{slave.name} has gained {ObedienceToAdd} pts of obedience.")
                print("he" if slave.genre == "man" else "she"+"'s now at", slave.obedience, "pts of obedience")
            else:
                print(slave.name, "is not enslaved by", self.name)
        else:
            print("I'm a slave and can't do anything if my master haven't ordered it to me...")
    def TrainOnShame(self, slave): # pov of owner/master
        if not self.enslaved:
            if slave in self.slaves:
                if slave.obedience >= 50:
                    ### Actions presented firstly as buttons after as imagebuttons
                    ### Next code won't be final code but a prototype to test without Ren'Py
                    ### and its dependencies
                    training = input("What to do? ")
                    if training == "1": ### Name will be replaced
                        efficiency = random.randint(1, 10)
                        if efficiency <= 5:
                            print("Work has been good, as always")
                        else:
                            print("Work has been better than usual")
                    elif training == "2": ### Name will be replaced
                        efficiency = random.randint(3, 10)
                        if efficiency <= 5:
                            print("Work has been bad")
                        else:
                            print("Work is good", "his" if slave.genre=="man"else "her", "formation is nearly completed")
            else:
                print(slave.name, "is not enslaved by", self.name)
        else:
            print("I'm a slave and can't do anything if my master haven't ordered it to me...")
    # TODO: Add different ways of training slave mentally or physically
    # TODO: Add Slave-Special System of Room, interacts, blocked and everything which can be used

    def OrderTo(self, slave, action, *args): # pov of owner/master
        if not self.enslaved:
            if slave in self.slaves:
                pass ### Here are stored all the actions used when npc is enslaved
                ### It will be implemented at the end
            else:
                print(slave.name, "is not enslaved by", self.name)
        else:
            print("I'm a slave and can't do anything if my master haven't ordered it to me...")

    def Free(self, slave): # pov of owner/master
        if not self.enslaved:
            if slave in self.slaves:
                self.slaves.remove(slave)
                slave.enslaved = False
                slave.free = True
                slave.owner = None

    #########################################################################
    ### NPC-Sim Methods including dynamic thoughts of every NPCs encountered
    #########################################################################
    def Encounters(self, who):
        if isinstance(who, NPC):
            if not who in self.encounters:
                self.encounters.append(who)
                if not who in self.thinks:
                    trust = 0; susp = 0; love = 0; anger = 0; fear = 0;
                ### Actions TODO:
                    ### See karma
                    ### See attachments (Factions)
                    ### See if already heard
                    ### See if pleases the npc
                    self.thinks[who] = {
                        "trust": trust,
                        "suspicion": susp,
                        "love": love,
                        "anger": anger,
                        "fear": fear,
                        "corruption": 0,
                        "loyalty": 0,
                    }
        else:
            print(who, "is not a NPC() object")

    ####################################################
    ### Taboo-Related Methods
    ####################################################
    def SetTaboo(self):
        for taboo in TabooList:
            self.taboos[taboo] = [False, True, False]

    def AddTaboo(self, taboo):
        if not self.taboos[taboo][0]:
            self.taboos[taboo][0] = True
        else:
            print(self.name, "already has the taboo")

    def BreakTaboo(self, taboo):
        if self.taboos[taboo][1]:
            self.taboos[taboo][1] = False
            renpy.log(self.name+" has the "+str(taboo.name)+" broken")
        else:
            print(self.name, "has already this taboo broken")

    def RandomTaboo(self):
        if self.taboos == []:
            self.SetTaboo()
        if type(len(self.taboos)/2) is int:
            x = random.randint(1, len(self.taboos)/2)
        else:
            x = random.randint(1, (int(len(self.taboos)/2)+1))
        y = 0; w = 0
        while y < x:
            z = random.randint(0, len(self.taboos)-1)
            z = TabooList[z];
            if not w == len(self.taboos):
                if z.contrary is not None:
                    if not self.taboos[z.contrary][0]:
                        if not self.taboos[z][0]:
                            self.taboos[z][0] = True
                            y += 1; w = 0
                        else: w += 1
                    else: w += 1
                else:
                    if not self.taboos[z][0]:
                        self.taboos[z][0] = True
                        y += 1; w = 0
                    else: w += 1
            else: break

    def HasTaboo(self, taboo):
        if self.taboos[taboo][0]:
            return True
        else:
            return False

    def HasBrokenTaboo(self, taboo):
        if not self.taboos[taboo][1]:
            return True
        else:
            return False

    ####################################################
    ### Map, Room Methods
    ####################################################
    def EnterRoom(self, room):
        if type(room) is environment.Room:
            room.people.append(self)
            self.inroom = room
            self.SearchPeopleInRoom()
            for entity in self.can_interact:
                self.Encounters(entity)
                entity.Encounters(self)
        else:
            print("The given room is not a Room() object")

    def ExitRoom(self):
        self.inroom.people.remove(self)
        self.inroom = None
        self.can_interact = []
        if self.interacts != None:
            self.interacts = None

    def SearchPeopleInRoom(self):
        l = []
        for people in self.inroom.people:
            if not people is self:
                l.append(people)
        if l != []:
            for people in l:
                self.can_interact = l

    def IsInRoom(self, room):
        if self.inroom is room:
            return True
        else:
            return False

    def InteractsWith(self, npc):
        if self.can_interact != None:
            if npc in self.can_interact:
                self.interacts = npc

    ####################################################
    ### Faction-Related Methods
    ####################################################
    def JoinFaction(self, faction):
        faction.members.append(self)
        self.free = False
        self.joined.append(faction)

    def QuitFaction(self, faction):
        if len(self.joined) != 0:
            if faction in self.joined:
                self.joined[self.joined.index(faction)].members.remove(self)
                self.joined.remove(faction)
                self.free = True
            else:
                print(self, "diddn't joined", faction, "faction")
        else:
            print(self, "didn't joined any factions")

########################################################
###
###
### User-Input needed methods | Used while developing
###
###
########################################################

    def CustomEyesColor(self):
        t = ""
        for color in NPC.eyes_color_list:
            if NPC.eyes_color_list.index(color) != len(NPC.eyes_color_list)-1:
                t += (color+", ")
            else:
                t += color
        print("The available colours for the eyes are:\n", t)
        choice = input("Enter the colour you chose: ")
        if choice in NPC.eyes_color_list:
            self.eyes_color = NPC.eyes_color_list[NPC.eyes_color_list.index(choice)]
            print(self, "now have", choice, "eyes")
        elif choice == "exit":
            return
        else:
            print(choice, "couldn't be found")
            self.CustomEyesColor()
    def CustomHairColors(self):
        t = ""
        for color in NPC.hair_color_list:
            if NPC.hair_color_list.index(color) != len(NPC.hair_color_list)-1:
                t == (color+", ")
            else:
                t += color
        print("The available colours for the hairs are:\n", t)
        choice = input("Enter the colour you chose: ")
        if choice in NPC.hair_color_list:
            self.hair_color = NPC.hair_color_list[NPC.hair_color_list.index(choice)]
            print(self, "have now", choice, "hairs")
        elif choice == "exit":
            return
        else:
            print(choice, "couldn't be found")
            self.CustomHairColors()
    def CustomHaircut(self):
        t = ""
        for haircut in NPC.haircut_list:
            if NPC.haircut_list.index(haircut) != len(NPC.haircut_list)-1:
                t += (haircut+", ")
            else:
                t += haircut
        print("The available haircuts are:\n", t)
        choice = input("Enter the haircut you chose: ")
        if choice in NPC.haircut_list:
            self.haircut = NPC.haircut_list[NPC.haircut_list.index(choice)]
            print(self, "have now a", choice, "haircut")
        elif choice == "exit":
            return
        else:
            print(choice, "couldn't be found")
            self.CustomHaircut()
    def CustomHairStyles(self):
        t = ""
        for style in NPC.hair_styles_list:
            if NPC.hair_styles_list.index(style) != len(NPC.hair_styles_list)-1:
                t += (style+", ")
            else:
                t += style
        print("The available hair styles are:\n", t)
        choice = input("Enter the hair style you chose: ")
        if choice in NPC.hair_styles_list:
            self.hair_style = NPC.hair_styles_list[NPC.hair_styles_list.index(choice)]
            print(self, "have now a", choice, "hair style")
        elif choice == "exit":
            return
        else:
            print(choice, "couldn't be found")
            self.CustomHairStyles()
    def CustomSkinColor(self):
        t = ""
        for colour in NPC.skin_color_list:
            if NPC.skin_color_list.index(colour) != len(NPC.skin_color_list)-1:
                t += (colour+", ")
            else:
                t += colour
        print("The available skin colours are:\n", t)
        choice = input("Enter the colour you chose: ")
        if choice in NPC.skin_color_list:
            self.skin_color = NPC.skin_color_list[NPC.skin_color_list.index(choice)]
            print(self, "have now a", choice, "skin")
        elif choice == "exit":
            return
        else:
            print(choice, "couldn't be found")
            self.CustomSkinColor()
    def CustomFacialPilosity(self):
        t = ""
        for pilosity_style in NPC.facial_pilosity_list:
            if NPC.facial_pilosity_list.index(pilosity_style) != len(NPC.facial_pilosity_list)-1:
                t += (pilosity_style+", ")
            else:
                t += pilosity_style
        print("The available face pilosity are:\n", t)
        choice = input("Enter the pilosity you chose: ")
        if choice in NPC.facial_pilosity_list:
            self.skin_color = NPC.facial_pilosity_list[NPC.facial_pilosity_list.index(choice)]
            print(self, "have now a", choice, "facial pilosity")
        elif choice == "exit":
            return
        else:
            print(choice, "couldn't be found")
            self.CustomFacialPilosity()
    def CustomBreastSize(self):
        t = ""
        for size in NPC.breast_size_list:
            if NPC.breast_size_list.index(size) != len(NPC.breast_size_list):
                t += (size+", ")
            else:
                t += size
        print("The available breast sizes are:\n", t)
        choice = input("Enter the size you chose: ")
        if choice in NPC.breast_size_list:
            self.breast_size = NPC.breast_size_list[NPC.breast_size_list.index(choice)]
            print(self, "now have", choice, "breasts")
        elif choice == "exit":
            return
        else:
            print(choice, "couldn't be found")
            self.CustomBreastSize()
    def CustomAssSize(self):
        t = ""
        for size in NPC.ass_size_list:
            if NPC.ass_size_list.index(size) != len(NPC.ass_size_list):
                t += (size+", ")
            else:
                t += size
        print("The available ass sizes are:\n", t)
        choice = input("Enter the size you chose: ")
        if choice in NPC.ass_size_list:
            self.ass_size = NPC.ass_size_list[NPC.ass_size_list.index(choice)]
            print(self, "now have a", choice, "ass")
        elif choice == "exit":
            return
        else:
            print(choice, "couldn't be found")
            self.CustomAssSize()



class MerchantMan(NPC):
    """
        This class is special and complicated to use due to the fact that
        all the methods are seen by the POV of the NPC.
        The Buy() method is used to sell an object to the merchant.
        The Sell() method is used to buy an object from the merchant.
    """
    #############################################
    ####    Actions Performed by our Merchants
    #############################################
    def Buy(self, seller, price, item, count=1): ### We buy item(s)
        if self.money >= price:
            self.money -= price
            seller.money += price
            if seller.inventory.Contains(item):
                seller.inventory.Remove(item)
                self.inventory.Add(item)
            print(self.name+"have bought "+item.name+" from "+seller.name+" for "+str(price)+" $")
            print("This Merchant have right now "+str(self.money)+" $")
            print(seller.name+" have "+str(seller.money)+" $")
        else:
            if self.genre == "man":
                print(self.name+" can't buy "+item.name+" because he don't have the money to buy it !")
            else:
                print(self.name+" can't buy "+item.name+" because she don't have the money to buy it !")

    def Sell(self, buyer, price, item, count=1): ### We sell item(s)
        if buyer.money >= price:
            self.money += price
            buyer.money -= price
            if self.inventory.Contains(item):
                self.inventory.Remove(item)
                buyer.inventory.Add(item)
            print(self.name+" have selled "+item.name+" to "+buyer.name+" for "+str(price)+" $")
            print("This Merchant have right now "+str(self.money)+" $")
            print( buyer.name+" have "+str(buyer.money)+" $")
        else:
            if buyer.genre == "man":
                print(buyer.name+" can't buy "+item.name+" because he don't have the money to buy it !")
            else:
                print(buyer.name+" can't buy "+item.name+" because she don't have the money to buy it !")

    def PresentItems(self, other):
        print("\nI have:")
        for item in self.inventory.content:
            print(f"- {item}: {self.inventory.content[item]['base-object'].price} $")
        choice = input("What do you want to do? ")
        if choice == "buy":
            choice = input("What do you buy? ")
            if choice in self.inventory.content:
                self.Sell(other, self.inventory.content[choice]["base-object"].price, self.inventory.content[choice]["base-object"])
        elif choice == "sell":
            other.ShowInventory()
            choice = input("What do you sell? ")
            if choice in other.inventory.content:
                self.Buy(other, other.inventory.content[choice]["base-object"].price, other.inventory.content[choice]["base-object"])
        else:
            print("Oh... See you next time then!")


class Travellers(NPC):
    def UpdateClass(self):
        self.money = 20000

class MerchantTravellers(Travellers, MerchantMan):
    def UpdateClassMerchTrav(self):
        self.name = "Merchant"
    def IsArriving(self):
        self.presents()
