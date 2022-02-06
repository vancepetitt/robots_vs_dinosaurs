from asyncio.proactor_events import _ProactorBasePipeTransport
from random import randrange


class Dinosaur:

    def __init__(self, name, health, attack_power, accuracy, description):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.accuracy = accuracy
        self.description = description

    def attack(self, robot):
        
        attempt = randrange(1,100)

        if attempt > self.accuracy:
            print(f'\n{self.name} misses the attack!\n')
        
        if attempt <= self.accuracy:         
            robot.health -= self.attack_power
      
        if attempt <= self.accuracy and robot.health > 0:
            print(f'\n{self.name} lands a prehistoric punch! {robot.name} is down to {robot.health} health!\n')
            print('--------------------------------------\n')

        if attempt <= self.accuracy and robot.health <= 0:
            print(f'\nWith a shower of sparks and grinding gears, {robot.name} powers down... for the last time!\n')
            print('--------------------------------------\n')
            


