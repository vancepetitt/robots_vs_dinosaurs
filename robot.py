from random import randrange
from unicodedata import name
from weapon import Weapon

class Robot:
    
    def __init__(self, name, health, weapon, description):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.description = description

    def attack(self, dinosaur):
        
        attempt = randrange(1,100)

        if attempt > self.weapon.accuracy:
            print(f'\n{self.name} misses the attack!\n')
        
        if attempt <= self.weapon.accuracy:         
            dinosaur.health -= self.weapon.attack_power

        if self.name == 'Titanium Jane':
            dinosaur.health -= 100
            print(f"Titanium Jane's shoulder blasters fire at the target! {dinosaur.name} is down to {dinosaur.health} health!\n")

        if attempt <= self.weapon.accuracy and dinosaur.health > 0:
            print(f'\n*CLANG...DIRECT HIT* {dinosaur.name} is down to {dinosaur.health} health!\n')
            print('--------------------------------------\n')

        elif attempt <= self.weapon.accuracy and dinosaur.health <= 0:
            print(f'\n{dinosaur.name} lets out one last mighty roar - and then falls in defeat!\n')
            print('--------------------------------------\n')
