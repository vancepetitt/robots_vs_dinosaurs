from unicodedata import name
from weapon import Weapon

class Robot:
    
    def __init__(self, name, health, weapon, description):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.description = description

    def attack(self, dinosaur):
        
        dinosaur.health -= self.weapon.attack_power

        if dinosaur.health > 0:
            print(f'\n*CLANG...DIRECT HIT* {dinosaur.name} is down to {dinosaur.health} health!\n')
            print('--------------------------------------\n')

        elif dinosaur.health <= 0:
            print(f'\n{dinosaur.name} lets out one last mighty roar - and then falls in defeat!\n')
            print('--------------------------------------\n')
