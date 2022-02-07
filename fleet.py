from robot import Robot
from weapon import Weapon

class Fleet:

    def __init__(self):
        self.fleet = []
        self.arsenal = []
        self.create_fleet()

    def create_fleet(self):
        
#weapons list - arsenal creation:

        a = Weapon('Supercharged Sword', 400, 90, 'This lethal melee weapon can slash a dinosaur with ease! Very accurate up close, and very deadly to machine and beast alike!')

        b = Weapon('Micro-Missile', 150, 100, 'A homing micro-missile. Very reliable as it locks on to the target for a guaranteed hit, but not designed for use against the thick hide of a dinosaur.')

        c = Weapon('Focused Fusion Launcher', 2000, 15, "A fusion launcher from a star cruiser, adapted for man-sized fighting robots. The recoil makes it easy to miss, but you can say goodbye to whatever this hits!.")

        d = Weapon('Laser Blasters', 300, 75, 'A barrage from an arm-mounted laser cannon. Fairly accurate with potential for mid-range damage')

        e = Weapon('Flyswatter', 1, 100, 'A flyswatter.')
        
        self.arsenal.append(a)
        self.arsenal.append(b)
        self.arsenal.append(c)
        self.arsenal.append(d)
        self.arsenal.append(e)




#Robots:        
        #weapon selection text:
        print("*******************************************************************************\n\n\n........As the robots approach the dinosaur homeworld from space, they have to select a weapon to get them online before the battle.\nThe robots have mutiple weapons from the fleet's arsenal that they can use to maximize their dino-slaying potential.\nEach weapon has an attack power and an accuracy that will ultimately determine it's performance in battle.\nWhen selecting a weapon please enter the following:")
        input('')
        print('To select a weapon, please enter the number corresponding to the choice you want. The following weapons are the current selections from the arsenal:\n')
        
        print(f'Enter "0" to select {self.arsenal[0].name}: {self.arsenal[0].description}\n')
        print(f'Enter "1" to select {self.arsenal[1].name}: {self.arsenal[1].description}\n')
        print(f'Enter "2" to select {self.arsenal[2].name}: {self.arsenal[2].description}\n')
        print(f'Enter "3" to select {self.arsenal[3].name}: {self.arsenal[3].description}\n')
        print(f'Enter "4" to select {self.arsenal[4].name}: {self.arsenal[4].description}\n')

        robot_1_weapon = int(input('Enter weapon choice for Blitz Bot (fast robot with low armor): '))
        robot_2_weapon = int(input('Enter weapon choice for Titanium Jane (average health and extra attack damage): '))
        robot_3_weapon = int(input('Enter weapon choice for X-Tanktron (maximum health): '))


        robot_1 = Robot('Blitz Bot', 500, self.arsenal[robot_1_weapon], 'Forgoing safety for speed by tossing non-essential components, Blitz Bot strikes fast. Give him an accurate weapon to get a lethal start to the round!')

        robot_2 = Robot('Titanium Jane', 750, self.arsenal[robot_2_weapon], 'A robot who eats dinosaurs for breakfast! With titanium plating and shoulder-mounted plasma blasters that fire in addition to whatever weapon she has, this heavy-metal heroine will blow you away!')

        robot_3 = Robot('X-Tanktron', 1700, self.arsenal[robot_3_weapon], "The fleet found X-Tanktron floating in space. Repaired for maximum durability, it is extremely heavily armored and can survive massive punishment, but slow.")

        self.fleet.append(robot_1)
        self.fleet.append(robot_2)
        self.fleet.append(robot_3)