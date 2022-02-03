from unicodedata import name
from weapon import Weapon

#weapons list
a = Weapon('Focused Fusion Launcher', 2000)

b = Weapon('Supercharged Sword', 400)

c = Weapon('Rocket Fists', 200)

d = Weapon('Flyswatter', 1)

e = Weapon('Laser Blasters', 300)


class Robot:

    def __init__(self, name, health, weapon):
        self.name = name
        self.health = health
        self.weapon = weapon


    def attack(self, dinosaur):
        pass