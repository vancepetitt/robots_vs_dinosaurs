from random import randrange
from dinosaur import Dinosaur
from fleet import Fleet
from herd import Herd

class Battlefield:

    def __init__(self):
        self.herd_1 = Herd()
        self.fleet_1 = Fleet()

    def run_game(self):
        self.display_welcome()
        self.dino_team_intro()
        self.robot_team_intro()
        self.battle()

    def display_welcome(self):
        print('******************************************************')
        print('ARE YOU READY TO RUMBLE!?')
        print('Today you have front row seats to a battle for the ages. The ROBOTS of THE FLEET are set to take on the DINOSAURS of THE LOST HERD!\nBefore we get started - lets introduce both teams...\n')
#        input('')

    def dino_team_intro(self):
        print('Fighting for the DINOSAURS...')
        print(f'{self.herd_1.herd[0].name}: {self.herd_1.herd[0].description}')
        print(f'{self.herd_1.herd[1].name}: {self.herd_1.herd[1].description}')
        print(f'{self.herd_1.herd[2].name}: {self.herd_1.herd[2].description}')
#        input('')

    def robot_team_intro(self):
        print('Fighting for the ROBOTS...')
        print(f'{self.fleet_1.fleet[0].name}: {self.fleet_1.fleet[0].description}')
        print(f'{self.fleet_1.fleet[1].name}: {self.fleet_1.fleet[1].description}')
        print(f'{self.fleet_1.fleet[2].name}: {self.fleet_1.fleet[2].description}')
#        input('')

    def battle(self):
        is_finished = False

        while is_finished == False:
            goes_first = randrange(1,3)
            if self.herd_1 == [] or self.fleet_1 == []:
                is_finished = True
                break

            elif goes_first == 1:
                goes_first = 0
                self.dino_turn()

            elif goes_first == 2:
                goes_first = 0
                self.robot_turn()
        
    def dino_turn(self):
        print('Dinosaurs attack first!')
        

    def robot_turn(self):
        print('Robots attack first!')


    def show_dino_opponent_options(self):
        pass

    def show_robot_opponent_options(self):
        pass

    def display_winners(self):
        if self.herd_1 == []:
            print('ROBOTS WIN!')
        elif self.fleet_1 == []:
            print('DINOSAURS WIN!')