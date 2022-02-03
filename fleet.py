from robot import Robot
from weapon import Weapon

#Robot list

jane = Robot('Titanium Jane', 700, weapon = input('Select a weapon for Titanium Jane: '))

blitz = Robot('Blitz Bot', 500, weapon = input('Select a weapon for Blitz Bot: '))

tank = Robot('X-Tanktron', 1500, weapon = input('Select a weapon for X-Tanktron: '))

class Fleet:

    def __init__(self):
        self.robots = []

    def create_fleet(self):
        self.robots.append(jane)
        self.robots.append(blitz)
        self.robots.append(tank)


