import random
import inventory
from datetime import datetime as dte

class Player:
    def __init__(self, name="player", age=19, color="#f9300c"):
        self.genre = random.choice(["fem", "man"])
        self.__name = name
        self.name = self.__name
        self.c = self.name
        self.color = color
        self.age = age
        self.life = 100
        self.money = 1000
        self.hadrelationship = []
        self.inventory = inventory.Inventory()

    ###################################
    ### Actions including speaking
    ###################################
    def SayStats(self):
        print("\nMy name is", self.name+".")
        print("I'm", self.age, "yo.")
        print("I'm a", "woman." if self.genre == "fem" else "guy.")
        print("My life is at", self.life, "hp.")
        print("I have", self.money, "$.")
        print(f"I had relations with {self.hadrelationship}." if not self.hadrelationship == [] else "I haven't had any relations yet.")

    ###################################
    ### Actions on Vars of Player
    ###################################
    def IsHurted(self, hp=random.randint(0,12)):
        self.life -= hp
        print("Ouch!")
    def IsHealing(self, hp=random.randint(0,12)):
        self.life += hp
        print("Ahh! It's better!")

    #####################################################
    ### Actions on Vars of others (Pnj, Monster classes)
    #####################################################
    def Hurt(self, other, hp=random.randint(0,12)):
        other.IsHurted(hp)
        print("Ha! I punched", other.name, "in the face!")
        print("He lost", hp, "hps" if hp > 1 else "hp")

    ###################################
    ### Ren'Py zone only
    ###################################
    ### Screens features
    def OpenInventory(self):
        for key, value in self.inventory.content.items():
            print(key, ":", value["base-object"])

    def ShowInventory(self):
        for item in self.inventory.content:
            print(f"- {item}")

### End of Player Class




def StoreData(variable, value):
    with open("cache.txt", "rt") as f:
        if not (variable+" : "+value+"\n") in f:
            with open("cache.txt", "at") as f:
                f.write(variable + " : " + value+"\n")
        else:
            print("Already written")

        f.close()
def RetrieveData():
    l = []
    dict = {}
    x = 0
    f=open("cache.txt","rt")
    for line in f:
        l = line.split(" : ")
    while x+1 < len(l):
        dict[l[x]] = l[x+1].replace("\n", "")
        x+=1
    print(dict)
def RetrieveSpecificData(data):
    l = []
    dict = {}
    x = 0
    with open("cache.txt", "rt") as f:
        for line in f:
            l = line.split(" : ")
        while x+1 < len(l):
            dict[l[x]] = l[x+1].replace("\n", "")
            x+=1
        if data in dict.keys():
            print(dict[data])
            return dict[data]
def PrintInventoryInFile(entity):
    file = open("test-log.txt", "at")
    file.write(f"Creation of {entity.name}'s inventory done the {str(dte.now())}: \n")
    for key, value in entity.inventory.content.items():
        file.write("    "+str(key)+" : "+str(value["base-object"])+"\n")
    file.write("\n")
    file.close()

def StoreObjectProperties(object):
    AllProperties = [p for p in dir(object) if isinstance(getattr(object, p), (int, float, str, list, dict))]
    AllValues = [getattr(object, p) for p in dir(object) if isinstance(getattr(object, p), (int, float, str, list, dict))]
    for (property, value) in zip(AllProperties, AllValues):
        if not property.startswith("__") and not property.endswith("__"):
            if not "DictProperty" in locals():
                DictProperty = {property: value}
            else:
                DictProperty[property] = value
            if not "persistent_names" in locals():
                persistent_names = {property: value}
            else:
                persistent_names["persistent."+property] = value
    return persistent_names
def StoreObjectPropertiesDict(object):
    Properties = {p:getattr(object, p) for p in dir(object) if isinstance(getattr(object, p), (int, float, str, list, dict))}
    return Properties
def TriObjectProperties(object):
        PropertyInt = [p for p in dir(object) if isinstance(getattr(object, p), int)]
        PropertyFloat = [p for p in dir(object) if isinstance(getattr(object, p), float)]
        PropertyStr = [p for p in dir(object) if isinstance(getattr(object, p), str)]
        PropertyList = [p for p in dir(object) if isinstance(getattr(object, p), list)]
        PropertyDict = [p for p in dir(object) if isinstance(getattr(object, p), dict)]

def AddProperty(object, property, value):
   object.property = value
   print(object.property)
   print(StoreObjectProperties(object))

def DefineVars(VariablesList):
    for variable, value in VariablesList.items():
        print(variable, "=", value)
