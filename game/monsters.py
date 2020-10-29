import random


class Monster:
    def __init__(self, name):
        self.life = 100
        self.name = name

    def IsHurted(self, hp=random.randint(0,12)):
        self.life -= hp
