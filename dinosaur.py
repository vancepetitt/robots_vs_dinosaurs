from asyncio.proactor_events import _ProactorBasePipeTransport
from random import randrange


class Dinosaur:

    def __init__(self, name, health, attack_power, description):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.description = description

    def attack(self, robot):
        
        robot.health -= self.attack_power

        if robot.health > 0:
            print(f'\n{self.name} lands a prehistoric punch! {robot.name} is down to {robot.health} health!\n')
            print('--------------------------------------\n')

        elif robot.health <= 0:
            print(f'\nWith a shower of sparks and grinding gears, {robot.name} powers down... for the last time!\n')
            print('--------------------------------------\n')
            


