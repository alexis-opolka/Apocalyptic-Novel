from lists import *
from renpy import Character
import random
import inventory
import environment
import renpy

"""
    This module contains the entire class for the PNJ, no more no less.
"""

class Pnj:
    """
        This class is only used for PNJs.
        We alternate the Point of View(POV) for the actions and sometimes have the two pov available for
        actions.
        For having the best reusability in no time, we mainly use the random module.

        Dependencies:\n
            - random module
            - lists module
            - inventory module
    """
    def __init__(self, name="???", color="#f9300c", genre="fem", minage=17, maxage=36, isenslaved=False, profile_image="images/pnj.png", font = "Avara.tff", dialogue_color = "#ffffff"):
        ### Strings Creator-defined
        self.c = Character(name, #The name to be displayed above the dialogue.
            what_font = font, #The font to be used for the character.
            who_font = font,
            color = color, #The colour of the character's NAME section
            what_color = dialogue_color) #The colour of the character's dialogue.
        self.age = random.randint(minage, maxage) # Aged Randomly defined between min and max age given when __init__() called
        self.name = name # Used to have the name of Object and Pnj
        self.color = color # Theoric use: Add it in the Character() function for having the pnj have this color
        self.genre = genre # Used to know the genre of pnj and conjugate phrases to male or female prefix
        self.profile_image = profile_image # used to show the image when pnj talks
        if self.genre == "fem":
            self.genren = "Woman" # Name used to properly define pnj's genre, here it's a female
        elif self.genre == "man":
            self.genren = "Man" # Name used to properly define pnj's genre, here it's a male
        else:
            self.genren = "Undefined" # Name used to properly define pnj's genre, here it's not given or pnj is non binary
        ### Strings Randomly defined
        self.hair_color = random.choice(HairColorList) # Store the hair color, after used to show layered images
        self.eyes_color = random.choice(EyesColorList) # Store the eyes color, after used to show layered images
        self.born_city = random.choice(CityList) # Store the city of born, after used to change value of price when enslaved
        ### Numbers: int/float | int preferred
        self.life = 100 # Life of pnj | It's used for doing things who needs life to be sure to be able to come back
        self.trust = 0 # Trust of pnj to someone | It's used to gain pnj in the team of Player
        self.suspicion = 0 # Suspicion of pnj to someone | It's used to determine the probability of doing smthng
        self.love = 0 # Love of pnj to someone
        self.anger = 0 # Anger of pnj to someone
        self.fear = 0 # Fear of pnj of someone or a group | Person is preferred
        self.corr = 0 # Corruption of pnj | Help to do illegal things with him
        self.loyalty = 0 # Loyalty of pnj to a camp, ideology or person
        self.inf = 30 # Infuence of pnj
        self.price = random.randint(150, 10000) # Price of pnj when he's enslaved, if not set manually
        self.money = 0 # Money the pnj have, currently 0
        self.will = random.randint(20, 100) # Will of pnj to do an action and the ability to be influenced or not | Can be broken with training if enslaved or can be upgraded with actions
        self.obedience = 0 # Obedience of pnj | Only used when self.enslaved is True
        self.shame = 100 # Shame of pnj | only used when self.enslave is True
        self.karma = 0 # Karma of pnj | Used to determine if can do bad or good things
        self.happiness = 100 # Happiness of pnj | Used to determine if is in depression or not
        ### Booleans
        if isenslaved == True:
            self.enslaved = True # pnj is a slave | Only used to know enslavement
            self.free = False # pnj is not free | Used to know certain amount of things: slavery, faction, prisoner, etc...
        elif isenslaved == False:
            self.enslaved = False # pnj isn't a slave | Only used to know enslavement
            self.free = True # pnj is free | Used to know certain amount of things: slavery, faction, prisoner, etc...
        self.dead = False # pnj is dead
        self.suicided = False # pnj suicided
        self.killed = False # pnj has been killed
        self.kidnapped = False # pnj has been kidnapped
        self.had_sex_with = False # if False pnj is a virgin otherwise he's not and the value is True
        ### None defined properties
        self.owner = None # Used to store object reference of Owner | Only used when pnj is enslaved, self.enslaved == True
        self.inroom = None # Used to store object reference of the Room
        self.interacts = None # Used to store object of the current PNJ/Player the pnj is interacting with
        ### Lists
        self.knows = [] # PNJ/Player is added when pnj hears of him/her
        self.encounters = [] # PNJ/Player is added when pnj speaks to them for the first time
        self.had_relationship = [] # Every relationships of pnj
        self.can_interact = [] # List of PNJ/Player with whom the pnj can interact, it's cleared when we quit the room | Used to dynamically interact with the PNJs of the Room
        self.slaves = [] # Every slaves of pnj
        ### Dictionnaries
        self.inventory = inventory.Inventory() # Inventory of pnj | property is in fact an object of class Inventory()
        self.thinks = {} ### Under Development: Dictionnary made to know the attributes given to each aquaintance
        self.taboos = {} # Here are placed the taboos of pnj as [Taboo-object, [If has, Broken Index,Player knows]]
        self.records = {} ### TODO: Develop a system to store the differents records of action | used to make statistics
        ### We call methods to set some base-properties
        self.SetTaboo()

    ######################################################
    ####    We have an impact on Vars of PNJ's
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

    def IsKilled(self):
        self.dead = True
        self.killed = True

    def IsSuicided(self):
        self.dead = True
        self.suicided = True

    def IsKidnapped(self):
        self.kidnapped = True

    def IsHavingSex(self, *names):
        self.had_sex_with = True
        self.had_relationship.append(names)

    #############################################################
    #### We print Information Or It's actions including speaking
    #############################################################
    def SayStats(self):
        if not self.enslaved:
            print("\nI'm a "+self.genren+".")
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

            if self.had_sex_with == False: print("I haven't had a relation with someone!")
            else: print("I had a relation with someone wouhou!")
        else:
            print("...")

    def SayMyRelations(self):
        if not self.enslaved:
            if self.had_relationship is None:
                print("I haven't had a relation with someone...")
            else:
                print(self.name,"I had relations with"+str(self.had_relationship))
        else:
            print("...")

    def talk(self):
        if not self.enslaved:
            print(random.choice(repliques))
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
    def CallLabel(self, mylabel):
        renpy.call(mylabel)

    #################################################
    ### Actions using images
    #################################################
    def ShowAt(self, position):
        renpy.show(self.profile_image)

    #################################################
    ### Randomization of Vars
    #################################################
    def RandomName(self):
        if self.genre == "fem":
            self.name = random.choice(WomenNames)
        elif self.genre == "man":
            self.name = random.choice(MaleNames)
        else:
            print("Genre is not properly defined")

    def RandomGender(self):
        self.genre = random.choice(["man", "fem"])

    def RandomMoney(self):
        self.money += random.randint(0, 8000)



    def RandomInfluence(self):
        self.inf += random.randint(0, 100)

    def RandomEnslavement(self):
        self.enslaved = random.choice(BooleanList)
        if self.enslaved == True:
            self.GetEnslaved()
        else:
            self.free = True

    def RandomInventory(self):
        x = random.randint(1, len(ItemList))
        while x > 0:
            self.inventory.Add(random.choice(ItemList))
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

    def GetEnslaved(self, owner): # pov of slave | Pnj is forced to
        if not self.enslaved:
            self.enslaved = True
            self.free = False
            owner.slaves.append(self)
            self.owner = owner
            self.InventoryMerge(owner)
        else:
            print(f"{self.name} is already enslaved, we can't enslave someone twice!")
    def Enslave(self, slave): # pov of owner | Pnj force someone
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
                pass ### Here are stored all the actions used when pnj is enslaved
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
    ### PNJ-Sim Methods including dynamic thoughts of every PNJs encountered
    #########################################################################
    def Encounters(self, who):
        if isinstance(who, Pnj):
            if not who in self.encounters:
                self.encounters.append(who)
                if not who in self.thinks:
                    self.thinks[who] = {
                        "trust": 0,
                        "suspicion": 0,
                        "love": 0,
                        "anger": 0,
                        "fear": 0,
                        "corruption": 0,
                        "loyalty": 0,
                    }
        else:
            print(who, "is not a Pnj() object")

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
            renpy.log("taboo broken")
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

    def SearchPeopleInRoom(self, step=False):
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

    def InteractWith(self, pnj):
        if self.can_interact != None:
            if pnj in self.can_interact:
                print("You are interacting with", pnj.name)
                self.interacts = pnj








class MerchantMan(Pnj):
    """
        This class is special and complicated to use due to the fact that
        all the methods are seen by the POV of the PNJ himself...
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


class Travellers(Pnj):
    def UpdateClass(self):
        self.money = 20000

class MerchantTravellers(Travellers, MerchantMan):
    def UpdateClassMerchTrav(self):
        self.name = "Merchant"
    def IsArriving(self):
        self.presents()
