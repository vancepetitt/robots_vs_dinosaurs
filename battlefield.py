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
        print('Fighting for the DINOSAURS...\n')
        print(f'{self.herd_1.herd[0].name}: {self.herd_1.herd[0].description}')
        print(f'{self.herd_1.herd[1].name}: {self.herd_1.herd[1].description}')
        print(f'{self.herd_1.herd[2].name}: {self.herd_1.herd[2].description}')
#        input('')

    def robot_team_intro(self):
        print('Fighting for the ROBOTS...\n')
        print(f'{self.fleet_1.fleet[0].name}: {self.fleet_1.fleet[0].description}')
        print(f'{self.fleet_1.fleet[1].name}: {self.fleet_1.fleet[1].description}')
        print(f'{self.fleet_1.fleet[2].name}: {self.fleet_1.fleet[2].description}')
#        input('')

    def battle(self):
        
        is_finished = False
        turn_count = 1

        while is_finished == False:
            goes_first = randrange(1,3)
            if self.fleet_1.fleet[0].health <= 0 and self.fleet_1.fleet[1].health <= 0 and self.fleet_1.fleet[2].health <=0:
                is_finished = True
                self.display_dinosaur_winners()

            elif self.herd_1.herd[0].health <= 0 and self.herd_1.herd[1].health <= 0 and self.herd_1.herd[2].health <= 0:
                is_finished = True
                self.display_robot_winners()

            elif goes_first == 1:
                print(f'TURN {turn_count}')
                turn_count += 1
                print('Dinosaurs attack first!\n')
                self.dino_turn()
                self.robot_turn()
                goes_first = 0

            elif goes_first == 2:
                print(f'TURN {turn_count}')
                turn_count += 1
                print('Robots attack first!\n')
                self.robot_turn()
                self.dino_turn()
                goes_first = 0

        
    def dino_turn(self):
        
        if self.herd_1.herd[0].health > 0:
            self.show_robot_opponent_options()
            target = int(input(f'\nWhich robot will {self.herd_1.herd[0].name} attack? ')) - 1
            self.herd_1.herd[0].attack(self.fleet_1.fleet[target])
 
        if  self.herd_1.herd[1].health > 0:
            self.show_robot_opponent_options()
            target = int(input(f'\nWhich robot will {self.herd_1.herd[1].name} attack? ')) - 1
            self.herd_1.herd[1].attack(self.fleet_1.fleet[target])
        
        if  self.herd_1.herd[2].health > 0:
            self.show_robot_opponent_options()
            target = int(input(f'\nWhich robot will {self.herd_1.herd[2].name} attack? ')) - 1
            self.herd_1.herd[2].attack(self.fleet_1.fleet[target])     

        

    def robot_turn(self):
               
        if  self.fleet_1.fleet[0].health > 0:
            self.show_dino_opponent_options()
            target = int(input(f'\nWhich dinosaur will {self.fleet_1.fleet[0].name} attack? ')) - 1
            self.fleet_1.fleet[0].attack(self.herd_1.herd[target])
        
        if  self.fleet_1.fleet[0].health > 0:
            self.show_dino_opponent_options()
            target = int(input(f'\nWhich dinosaur will {self.fleet_1.fleet[1].name} attack? ')) - 1
            self.fleet_1.fleet[1].attack(self.herd_1.herd[target])
        
        if  self.fleet_1.fleet[0].health > 0:
            self.show_dino_opponent_options()
            target = int(input(f'\nWhich dinosaur will {self.fleet_1.fleet[2].name} attack? ')) - 1
            self.fleet_1.fleet[2].attack(self.herd_1.herd[target])


    def show_dino_opponent_options(self):

        herd_defeated = False
        while herd_defeated == False:

            if self.herd_1.herd[0].health <= 0 and self.herd_1.herd[1].health <= 0 and self.herd_1.herd[2].health <= 0:
                herd_defeated = True
                break 
            
            if self.herd_1.herd[0].health > 0:
                print(f'Enter "1" to attack {self.herd_1.herd[0].name} ({self.herd_1.herd[0].health} health)')
            
            if self.herd_1.herd[1].health > 0:
                print(f'Enter "2" to attack {self.herd_1.herd[1].name} ({self.herd_1.herd[1].health} health)')
            
            if self.herd_1.herd[2].health > 0:
                print(f'Enter "3" to attack {self.herd_1.herd[2].name} ({self.herd_1.herd[2].health} health)')
                break

    def show_robot_opponent_options(self):

        fleet_defeated = False
        while fleet_defeated == False:
            
            if self.fleet_1.fleet[0].health <= 0 and self.fleet_1.fleet[1].health <= 0 and self.fleet_1.fleet[1].health <=0:
                fleet_defeated = True
                break    
            
            if self.fleet_1.fleet[0].health > 0:
                print(f'Enter "1" to attack {self.fleet_1.fleet[0].name} ({self.fleet_1.fleet[0].health} health)')
            
            if self.fleet_1.fleet[1].health > 0:
                print(f'Enter "2" to attack {self.fleet_1.fleet[1].name} ({self.fleet_1.fleet[1].health} health)')
            
            if self.fleet_1.fleet[2].health > 0:
                print(f'Enter "3" to attack {self.fleet_1.fleet[2].name} ({self.fleet_1.fleet[2].health} health)')
                break


    def display_robot_winners(self):
            print('ROBOTS WIN!')

    def display_dinosaur_winners(self):
            print('DINOSAURS WIN!')