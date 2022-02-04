from robot import Robot
from weapon import Weapon

class Fleet:

    def __init__(self):
        self.fleet = []
        self.create_fleet()

    def create_fleet(self):
        
#weapons list
        a = Weapon('Focused Fusion Launcher', 2000)

        b = Weapon('Supercharged Sword', 400)

        c = Weapon('Rocket Fists', 100)

        d = Weapon('Flyswatter', 1)

        e = Weapon('Laser Blasters', 300)

#Robots:
        robot_1 = Robot('Titanium Jane', 750, e)
        robot_2 = Robot('Blitz Bot', 500, b)

        robot_3 = Robot('X-Tanktron', 1500, c)

        # print('The robots have mutiple weapons they can use to maximize their dino-saying potential.')
        # print()
        # print('When selecting weapons:')
        # print(' Enter "a" for the ')
        self.fleet.append(robot_1)
        self.fleet.append(robot_2)
        self.fleet.append(robot_3)




