from unicodedata import name

from weapon import Weapon

class Robot:

    def __init__(self, name, health, weapon):
        self.name = name
        self.health = health
        self.weapon = Weapon()

    def attack(self, dinosaur):
        pass