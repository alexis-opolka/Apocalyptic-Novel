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
        
    def ChangeDay(self):
        self.clock.AddDay()
    
    def ChangeMonth(self):
        self.clock.AddMonth()

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
        self.year = 2021
        self.all_months = [
            #["month_name", max_days, place_in_year]
            ### "month_name" is displayed to the player
            ### max_days is the number of days before we go to the next month
            ### place_in_year is displayed as a short date to the player
            ["January", 31, 1], ["February", 28, 2],
            ["March", 31, 3], ["April", 30, 4],
            ["May", 31, 5], ["June", 30, 6],
            ["July", 31, 7], ["August", 31, 8],
            ["September", 30, 9], ["October", 31, 10],
            ["November", 30, 11], ["December", 31, 12]]
        self.all_days = [
            #["day_name", position_in_week]
            ### "day_name" is displayed to the player
            ### position_in_week is used to say which day we are, the 1st, 2nd, 4th, etc...
            ["Monday", 1], ["Tuesday", 2],
            ["Wednesday", 3], ["Thursday", 4],
            ["Friday", 5], ["Saturday", 6],
            ["Sunday", 7]]
        self.all_times = [
            #["time_name", start_time_hour, end_time_hour]
            ### "time_name" is displayed to the player
            ### start_time_hour is the hour where the time starts | used to set the hour if need
            ### end_time_hour is the hour where the time ends | used to see if we need to change the time of the day
            ["morning", 6, 10], ["noon", 11, 12], 
            ["afternoon", 13, 16], ["evening", 17, 21], 
            ["night", 22, 29]] #We set 30 instead of 6 because it creates bugs otherwise
        self.nbr_day = 1 ### It's the number of days in the month, the 1st, the 2nd, etc...
        ### self.minutes is divided in four parts, 0=15min, 1=30min, 2=45min, 3=60min
        ### Each "quick" actions will take from 1 to 3 minutes, it means from 15min to 45min
        ### If it takes more than 3 to be accomplished hours are preferred to use.
        self.minutes = 0
        ### self.curr_month is used to have a step for not having to search which month we are
        self.curr_month = self.all_months[2]
        ### self.curr_day is used to have a step for not having to search which day we are
        self.curr_day = self.all_days[0]
        ### self.curr_time is used to have a step for not having to search which time of the day we are
        self.curr_time = self.all_times[0]
        self.month = self.curr_month[0] ### self.month is displayed to the player
        self.day = self.curr_day[0] ### self.day is displayed to the player
        self.time = self.all_times[0][0] ### self.time is displayed to the player
        self.hour = self.all_times[0][1] ### self.hour is displayed to the player
        self.min = 0 ### self.min is displayed to the player
        self.short_month = self.curr_month[2] ### self.short_month is used to display the short version of the date

    ### Setting methods
    def SetHour(self, hour=6):
        self.hour = hour
        
    def SetDay(self, day):
        self.day = day

    def SetNbrDay(self, day):
        self.nbr_day = day

    def SetMonth(self, month):
        self.month = month

    def SetYear(self, year):
        self.year = year

    ### Addition methods
    def AddMinutes(self, minutes=1):
        if self.minutes+1 > 3:
            self.AddHour()
            self.minutes = 0
            self.min = 0
        else:
            self.minutes += 1
            self.min += 15

    def AddHour(self, hour=1):
        """
            It adds the given hour amount if not the default value is taken.\n
            We then look if the new hour is greater than the max_hour the time has
            If True we ask wich time it is and we set the new time, the next one.
        """
        self.hour += hour
        if self.hour == 24:
            self.AddDay()
        if self.hour > self.curr_time[2]:
            if (self.all_times.index(self.curr_time)+hour) != len(self.all_times):
                self.curr_time = self.all_times[self.all_times.index(self.curr_time)+hour]
            else:
                self.curr_time = self.all_times[0]
            self.time = self.curr_time[0]
            if self.curr_time is self.all_times[0]:
                self.SetHour(self.curr_time[1]) ### The hour continues even after 24 (midnight) to 30,
                                                ### at morning it's set as the start hour of the time

    def AddDay(self, day=1):
        """
            We add the given amount of days, if not the default value is taken. \n
            We then look if the number of days is not greater than the max_days of the month.
            If True we add one month.
        """
        self.nbr_day += day
        if self.nbr_day > self.curr_month[1]:
            self.AddMonth()

    def AddMonth(self, month=1):
        """
            We add the given amount of months, if not the default value is taken. \n
            We then look if the next month is still a month of the current year.
            If True we add one month.
            If False we add one year.
            After we reset the number of days to 1.
        """
        if (self.all_months.index(self.curr_month)+month) != len(self.all_months):
            self.curr_month = self.all_months[self.all_months.index(self.curr_month)+month]
        else:
            self.AddYear()
        self.nbr_day = 1
        self.short_month = self.curr_month[2] ### Added otherwise the variable is not updated
                                              ### Even if the var is defined using the other one which is updated

    def AddYear(self, year=1):
        """
            We add the given amount of years, if not the default value is taken. \n
            We then set the current month as the first one (index 0).
        """
        self.year += year
        self.curr_month = self.all_months[0]


    ### Substraction methods
    def SubstHour(self, hour=1):
        self.hour -= hour

    def SubstDay(self, day=1):
        self.nbr_day -= day

    ### Output methods
    def ShowTimenHourInShell(self):
        if (self.hour - 24) < 0:
            print("{}:{}, {}".format(self.hour, "0"+str(self.min) if self.min == 0 else self.min, self.time))
        else:
            print("{}:{}, {}".format((self.hour-24), "0"+str(self.min) if self.min == 0 else self.min, self.time))
            

    def ShowAllInShell(self):
        if self.nbr_day < 10:
            if self.short_month < 10:
                print(f"0{self.nbr_day}/0{self.short_month}/{self.year}")
            else:
                print(f"0{self.nbr_day}/{self.short_month}/{self.year}")
        elif self.short_month < 10:
            print(f"{self.nbr_day}/0{self.short_month}/{self.year}")
        else:
            print(f"{self.nbr_day}/{self.short_month}/{self.year}")