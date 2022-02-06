from robot import Robot
from weapon import Weapon

class Fleet:

    def __init__(self):
        self.fleet = []
        self.create_fleet()

    def create_fleet(self):
        
#weapons list
        a = Weapon('Focused Fusion Launcher', 2000, 15)

        b = Weapon('Supercharged Sword', 400, 90)

        c = Weapon('Micro-Missile', 150, 100)

        d = Weapon('Flyswatter', 1, 100)

        e = Weapon('Laser Blasters', 300, 75)

#Robots:
        robot_2 = Robot('Titanium Jane', 750, e, 'A robot who eats dinosaurs for breakfast! With titanium plating and repeating laser blasters, this heavy-metal heroine will blow you away!')

        robot_1 = Robot('Blitz Bot', 500, b, 'Forgoing safety for speed by tossing non-essential components, Blitz Bot strikes fast, and strikes hard with the help of his Supercharged Shock Sword!')

        robot_3 = Robot('X-Tanktron', 1500, c, "The fleet found X-Tanktron floating in space. Repaired for maximum durability, it is heavily armored and delivers heat-seeking Micro-Missiles!")

        # print('The robots have mutiple weapons they can use to maximize their dino-saying potential.')
        # print()
        # print('When selecting weapons:')
        # print(' Enter "a" for the ')
        self.fleet.append(robot_1)
        self.fleet.append(robot_2)
        self.fleet.append(robot_3)