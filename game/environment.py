import datetime

class World:
    """
       World class is made to support different systems \n
       She takes the "map" system with different places and the possibility to have
       a certain amount of people/pnj in it. \n
       It manages the economic system with the different money available and the demand/support interaction. \n
       It manages some others systems not developed yet.
    """
    def __init__(self):
        self.envs = []
        self.datetime = str(datetime.datetime.now)

class Environment:
    def __init__(self, world, landscape="city"):
        self.type = landscape
        self.places = []
        if type(world) is World:
            world.envs.append(self)
        else:
            print("The world given is not an object of the World() class")
            exit()


class Room:
        def __init__(self, environment, name="Place"):
            if type(environment) is Environment:
                environment.places.append(self)
            else:
                print("The environment given is not an object of the Environment() class")
                print("We can't initialize a Place() object if we don't have any Environment() to be placed in...")
                exit()
            self.name = name
            self.people = []

        def Ask(self):
            print("Well... It seems to work...")


class Clock:
    def __init__(self):
        self.all_times = [["morning", 6, 11], ["noon", 11, 13], ["afternoon", 13, 20], ["?", 20, 21], ["night", 21, 6]]
        self.time = self.all_times[0][0]
        self.hour = self.all_times[0][1]
