import datetime
import time

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
        self.clock = Clock()
    
    def ChangeHour(self):
        self.clock.AddHour()
        if self.clock.hour > self.clock.curr_time[2]:
            if self.clock.time == self.clock.all_times[0][0]:
                self.clock.time = self.clock.all_times[1][0]
                self.clock.curr_time = self.clock.all_times[1]
            elif self.clock.time == self.clock.all_times[1][0]:
                self.clock.time = self.clock.all_times[2][0]
                self.clock.curr_time = self.clock.all_times[2]
            elif self.clock.time == self.clock.all_times[2][0]:
                self.clock.time = self.clock.all_times[3][0]
                self.clock.curr_time = self.clock.all_times[3]
            elif self.clock.time == self.clock.all_times[3][0]:
                self.clock.time = self.clock.all_times[4][0]
                self.clock.curr_time = self.clock.all_times[4]
            elif self.clock.time == self.clock.all_times[4][0]:
                self.clock.time = self.clock.all_times[0][0]
                self.clock.curr_time = self.clock.all_times[0]
                self.clock.SetHour(7)
            else:
                self.clock.time = self.clock.all_times[0][0]
        self.clock.ShowTimenHourInShell()
        time.sleep(0.5)
        self.ChangeHour()
        
    def ChangeDay(self):
        pass
    
    def ChangeMonth(self):
        pass

class Environment:
    def __init__(self, world, landscape="city"):
        self.type = landscape
        self.places = []
        if type(world) is World:
            world.envs.append(self)
        else:
            print("The given world is not an object of the World() class")
            exit()


class Room:
        def __init__(self, environment, name="Place"):
            if type(environment) is Environment:
                environment.places.append(self)
            else:
                print("The given environment is not an object of the Environment() class")
                print("We can't initialize a Place() object if we don't have any Environment() to be placed in...")
                exit()
            self.name = name
            self.people = []

        def Ask(self):
            print("Well... It seems to work...")


class Clock:
    def __init__(self):
        self.all_months = [
            #["month_name", max_days, place_in_year]
            ["January", 31, 1],
            ["February", 28, 2],
            ["March", 31, 3],
            ["April", 30, 4],
            ["May", 31, 5],
            ["June", 30, 6],
            ["July", 31, 7],
            ["August", 31, 8],
            ["September", 30, 9],
            ["October", 31, 10],
            ["November", 30, 11],
            ["December", 31, 12]]
        self.all_days = [
            #["day_name", position_in_week]
            ["Monday", 1],
            ["Tuesday", 2],
            ["Wednesday", 3],
            ["Thursday", 4],
            ["Friday", 5],
            ["Saturday", 6],
            ["Sunday", 7]]
        self.all_times = [
            #["time_name", start_time_hour, end_time_hour]
            ["morning", 6, 11], 
            ["noon", 11, 13], 
            ["afternoon", 13, 20], 
            ["evening", 20, 21], 
            ["night", 21, 30]] #We set 30 instead of 6 because it creates bugs otherwise
        self.curr_month = self.all_months[2]
        self.curr_day = self.all_days[0]
        self.curr_time = self.all_times[0]
        self.year = 2021
        self.month = self.curr_month[0]
        self.day = self.curr_day[0]
        self.time = self.all_times[0][0]
        self.hour = self.all_times[0][1]
        self.short_month = self.curr_month[2]
        self.short_day = self.curr_day[1]

    def SetHour(self, value=6):
        self.hour = value

    def AddHour(self, value=1):
        self.hour += value

    def SubstHour(self, value=1):
        self.hour -= value

    ### Output methods
    def ShowTimenHourInShell(self):
        if self.time != self.all_times[4][0]:
            print("{}: {}h".format(self.time, self.hour))
        else:
            if (self.hour - 24) < 0:
                print("{}: {}h".format(self.time, self.hour))
            else:
                print("{}: {}h".format(self.time, (self.hour-24)))

    def ShowAllInShell(self):
        if self.short_day < 10:
            if self.short_month < 10:
                print(f"{self.hour}, {self.time}, 0{self.short_day}/0{self.short_month}/{self.year}")
            else:
                print(f"{self.hour}, {self.time}, 0{self.short_day}/{self.short_month}/{self.year}")
        elif self.short_month < 10:
            print(f"{self.hour}, {self.time}, {self.short_day}/0{self.short_month}/{self.year}")
        else:
            print(f"{self.hour}, {self.time}, {self.short_day}/{self.short_month}/{self.year}")