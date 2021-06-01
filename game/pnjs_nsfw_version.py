import random
from lists import *
import inventory

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
    def __init__(self, name="Pnj", color="#f9300c", genre="fem", minage=17, maxage=36, isenslaved=False, profile_image="images/pnj.png", *args, **kwargs):
        ### Strings Creator-defined
        self.c = name # Property used to talk, mainly with dialogues in Ren'Py
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
        self.owner = None # Used to store object reference of Owner | Only used when pnj is enslaved, self.enslaved == True
        self.waylostvirginity = None # Used to store the way pnj lost his/her virginity
        self.waylostanalvirginity = None # Used to store the way pnj lost his/her anal virginity
        ### Strings Randomly defined
        self.hair_color = random.choice(HairColorList) # Store the hair color, after used to show layered images
        self.eyes_color = random.choice(EyesColorList) # Store the eyes color, after used to show layered images
        self.born_city = random.choice(CityList) # Store the city of born, after used to change value of price when enslaved
        ### Numbers: int/float | int preferred
        self.life = 100 # Life of pnj | It's used for doing things who needs life to be sure to be able to come back
        self.trust = 0 # Trust of pnj to someone | It's used to gain pnj in the team of Player
        self.suspicion = 0 # Suspicion of pnj to someone | It's used to determine the probability of doing smthng
        self.love = 0 # Love of pnj to someone
        self.angry = 0 # Anger of pnj to someone
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
        #### Sex-Related
        self.analcount = 0
        self.sexcount = 0
        self.blowjobcount = 0
        self.masturbationcount = 0
        self.orgasmcount = 0
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
        self.hadsexwith = False # if False pnj is a virgin otherwise he's not and the value is True
        self.hastaboonude = False # if False pnj wants to hide its nude parts, True only if self.shame is 0 the pnj don't care if he's naked | Can be broken in multiple occasions
        self.hastaboosex = False # if False pnj don't wants to have sex with anyone, if True pnj accepts more easily | Can be broken in multiple occasions 
        self.hastaboobj = False # if False pnj don't wants to have oral sex with anyone, if True pnj accepts more easily | Can be broken in multiple occasions
        self.hastabookill = False # if False pnj don't wants to kill someone, if True pnj can kill somebody | Can be broken after first kill or training
        self.hastabooegality = False # if False pnj believes in egality between human beings, if True pnj believes there's someone above someone else | Is broken when enslaved or enslave someone
        self.hastaboocapitalism = False # if False pnj believes in a capitalism system, if True pnj believes there's a better system than a capitalist one | Can be broken if joins a faction
        ### Lists
        self.hadrelationship = [] # Every relationships of pnj
        self.slaves = [] # Every slaves of pnj
        ### Dictionnaries
        self.inventory = inventory.Inventory() # Inventory of pnj | property is in fact an object of class Inventory()

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
        self.suspicion += amount
    def SustSuspicion(self, amount):
        self.suspicion -= amount

    def AddLove(self, amount):
        self.love += amount
    def SustLove(self, amount):
        self.love -= amount

    def AddAngry(self, amount):
        self.angry += amount
    def SustAngry(self, amount):
        self.angry -= amount

    def AddFear(self, amount):
        self.fear += amount
    def SustFear(self, amount):
        self.fear -= amount

    def AddCorruption(self, amount):
        self.corr += amount
    def SustCorruption(self, amount):
        self.corr -= amount

    def AddLoyalty(self, amount):
        self.loyalty += amount
    def SustLoyalty(self, amount):
        self.loyalty -= amount

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

    def IsHavingSexPls(self, *names):
        self.hadsexwith = True
        self.hadrelationship.append(names)

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

            if self.hadsexwith == False: print("I haven't had a relation with someone!")
            else: print("I had a relation with someone wouhou!")
        else:
            print("...")

    def SayMyRelations(self):
        if not self.enslaved:
            if self.hadrelationship is None:
                print("I haven't had a relation with someone...")
            else:
                print(self.name,"I had relations with"+str(self.hadrelationship))
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
    ### RandomiAntion of Vars
    #################################################
    def RandomName(self):
        if self.genre == "fem":
            self.name = random.choice(WomenNames)
        elif self.genre == "man":
            self.name = random.choice(MaleNames)
        else:
            print("Genre is not properly defined")

    def RandomGender(self):
        self.genre = random.choice("man", "fem")

    def RandomMoney(self):
        self.money += random.randint(0, 8000)

    def RandomSuspicion(self):
        self.suspicion += random.randint(0, 100)

    def RandomLove(self):
        self.love += random.randint(0, 100)

    def RandomAngry(self):
        self.love += random.randint(0, 100)

    def RandomFear(self):
        self.fear += random.randint(0, 100)

    def RandomCorruption(self):
        self.corr += random.randint(0, 100)

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
    def InventoryOpen(self):
        if not self.enslaved:
            for key, value in self.inventory.content.items():
                print(key, ":", value["base-object"])
        else:
            print("As a slave, I don't have any possession...")
    def InventoryShow(self):
        if not self.enslaved:
            for key, value in self.inventory.content.items():
                print(key, ":", value)
        else:
            print("As a slave I don't have any possessions...")
    
    def InventoryMerge(self, receiver):
        for key, item in self.inventory.content.items():
            receiver.inventory.Add(item["base-object"])

    ##################################################
    ### Slave Methods
    ##################################################
    def SetSlavePrice(self, slave, price):
        if not self.enslaved:
            slave.price = price
        else:
            print("I'm a slave and can't do anything if my master haven't ordered it to me...")

    def GetEnslaved(self, owner): ### pov of slave | Pnj is forced to
        if not self.enslaved:
            self.enslaved = True
            self.free = False
            owner.slaves.append(self)
            self.owner = owner
            self.InventoryMerge(owner)
        else:
            print(f"{self.name} is already enslaved, we can't enslave someone twice!")
    def Enslave(self, slave): ### pov of owner | Pnj force someone
        if not slave.enslaved:
            slave.enslaved = True
            self.free = False
            self.slaves.append(slave)
            slave.owner = self
            slave.InventoryMerge(self)
        else:
            print(f"{slave.name} is already enslaved, we can't enslave someone twice!")

    def PresentSlave(self): ### pov of owner
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
    def PresentOwner(self): ### pov of slave
        print("I'm the slave of", self.owner.name)
        print("Ask to","him" if self.owner.genre=="man" else "her", "for more informations...", end="\n\n")

    def Train(self, slave):
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
    def TrainOnShame(self, slave):
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

    def OrderTo(self, slave, action, *args):
        if not self.enslaved:
            if slave in self.slaves:
                pass ### Here are stored all the actions used when pnj is enslaved
                ### It will be implemented at the end
            else:
                print(slave.name, "is not enslaved by", self.name)
        else:
            print("I'm a slave and can't do anything if my master haven't ordered it to me...")

    ##################################################
    ### Sex-Related Methods
    ##################################################
    def LostVirginity(self, way):
        posspro = "his" if self.genre == "man" else "her"
        pro = "he" if self.genre == "man" else "she"
        self.waylostvirginity = str(f"When {pro} lost {posspro} virginity {pro} was {way}")
    
    def LostAnalVirginity(self, way):
        posspro = "his" if self.genre == "man" else "her"
        pro = "he" if self.genre == "man" else "she"
        self.waylostanalvirginity = str(f"When {pro} lost {posspro} anal virginity {pro} was {way}")

    def MakeOralSex(self, person):
        if not self.enslaved:
            if person.enslaved:
                if person.shame <= 65:
                    print("As a slave", person.name, "has been ordered to have oral sex and dit it whith", self.name)
                elif person.obedience >= 40:              
                        print("As a slave", person.name, "has been ordered to have oral sex and did it with", self.name)
                        print("She now knows how to do it and it seems to be more pleasant for her each time...")
                else:
                    print(person.name, "don't want to do it and haven't did it.")           
            elif person.love >= 60:
                print(person.name, "loves you and had oral sex with you.")
            elif person.will <= 35:
                print(person.name, "had been influenced by you and finally accepted to have oral sex")
        else:
            print(self.name, "is enslaved and can't do anything if it haven't been ordered by", "her" if self.genre == "fem" else "his", "master")
    def MakeSex(self, person):
        if not self.enslaved and not self.genre == "man" and not person.genre == "man":
            if person.enslaved:
                if person.shame <= 50:
                    if not person.hadsexwith:
                        print("As a slave", person.name, "has been ordered to have sex and did it with", self.name)
                        print("She grimaced because it was her first time")
                        print("She was a virgin, she's not anymore...")
                        person.LostVirginity("forced")
                    else:
                        print("As a slave", person.name, "has been ordered to have sex and did it with", self.name)
                        print("She now know how to do it and it seems to be more pleasant for her each time...")
                else:
                    if person.obedience >= 80:              
                        if not person.hadsexwith:
                            print(person.name, "is not happy about that but has been well trained and did it though")
                            print("She grimaced because it was her first time")
                            print("She was a virgin, she's not anymore...")
                            person.LostVirginity("forced")
                        else:
                            print("As a slave", person.name, "has been ordered to have sex and did it with", self.name)
                            print("She now knows how to do it and it seems to be more pleasant for her each time...")
                    else:
                        print(person.name, "don't do it")
            elif person.love >= 75:
                if not person.hadsexwith:
                    print(person.name, "loves you and had lost", "her" if person.genre == "fem" else "his", "virginity to you")
                    person.LostVirginity("loved")
                else:
                    print(person.name, "loves you and had sex with you.")
            elif person.will <= 25:
                if not person.hadsexwith:
                    print(person.name, "had been influenced by you and finally accepted to have sex")
                    print("Because of that", "she" if person.genre == "fem" else "he", "lost", "her" if person.genre == "fem" else "his", "virginity")
                    person.LostVirginity("influenced")
                else:
                    print(person.name, "had been influenced by you and finally accepted to have sex")
        else:
            if self.enslaved:
                print(self.name, "is enslaved and can't do anything if it haven't been ordered by", "her" if self.genre == "fem" else "his", "master")
            else:
                print(self.name, "and", person.name, "can,'t have sex because the both are Men")
    def MakeAnalSex(self, person):
        if not self.enslaved:
            if person.enslaved:
                if person.shame <= 12:
                    if not person.hadanalsexwith:
                        print("As a slave", person.name, "has been ordered to have anal sex and dit it whith", self.name)
                        print("It hurted", "her" if person.genre =="fem" else "him", "at first but the more", self.name, "entered and got out of this slave ass the better it became")
                        print("She" if person.genre == "fem" else "He", "was a virgin, not anymore...")
                        person.LostAnalVirginity("forced")
                    else:
                        print("As a slave", person.name, "has been ordered to have sex and did it with", self.name)
                        print("She now know how to do it and it seems to be more pleasant for her each time...")
                elif person.obedience >= 80:              
                        if not person.hadsexwith:
                            print(person.name, "is not happy about that but has been well trained and did it though")
                            print("She grimaced because it was her first time")
                            print("She was a virgin, she's not anymore...")
                            person.LostAnalVirginity("forced")
                        else:
                            print("As a slave", person.name, "has been ordered to have anal sex and did it with", self.name)
                            print("She now knows how to do it and it seems to be more pleasant for her each time...")
                else:
                    print(person.name, "don't want to do it and haven't did it.")           
            elif person.love >= 90:
                if not person.hadsexwith:
                    print(person.name, "loves you and had lost", "her" if person.genre == "fem" else "his", "virginity to you")
                    person.LostAnalVirginity("loved")
                else:
                    print(person.name, "loves you and had anal sex with you.")
            elif person.will <= 25:
                if not person.hadsexwith:
                    print(person.name, "had been influenced by you and finally accepted to have sex")
                    print("Because of that", "she" if person.genre == "fem" else "he", "lost", "her" if person.genre == "fem" else "his", "virginity")
                    person.LostVirginity("influenced")
                else:
                    print(person.name, "had been influenced by you and finally accepted to have anal sex")
        else:
            print(self.name, "is enslaved and can't do anything if it haven't been ordered by", "her" if self.genre == "fem" else "his", "master")







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
