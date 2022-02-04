from unicodedata import name
from weapon import Weapon

class Robot:
    
    def __init__(self, name, health, weapon, description):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.description = description

    def attack(self, dinosaur):
        pass
