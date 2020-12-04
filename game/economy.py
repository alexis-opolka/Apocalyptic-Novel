import time
import random
from multiprocessing import Process
import os
import math

class GlobalMarketPlace:
    """
        Class englobing every item and its price on the entire world,
        Picks the average between every EnvironmentMarketPlace() to have a price
        representating the global price of an item in the World()
    """
    def __init__(self):
        #pass ### Placeholder, TODO: Create the system
        need = 50
        conso = 30
        self.test = int(50+math.atan(float(need)/float(conso))*100/math.pi)
        print(self.test)

class EnvironmentMarketPlace:
    """
        Class used to store and manage the price of items in a same Environment()
    """
    def __init__(self):
        pass ### Placeholder, TODO: Create the system

class FactionMarketPlace:
    """
        Class used to store a special MarketPlace only used by the members of a Faction()
        If PNJ/Player interacts with a merchant in a Faction(), the merchant determines which MarketPlace() he'll use.
        If it's in a territory wich belongs to the particular faction or belongs to an allied faction, the
        FactionMarketPlace() is preferred, on the contrary in a neutral territory the system used is the
        EnvironmentMarketPlace().
    """
    def __init__(self):
        pass ### Placeholder, TODO: Create the system
