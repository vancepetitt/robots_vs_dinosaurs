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

    def display_welcome(self):
        print('******************************************************')
        print('ARE YOU READY TO RUMBLE!?')
        print('Today you have front row seats to a battle for the ages. The ROBOTS of THE FLEET are set to take on the DINOSAURS of THE LOST HERD!\nBefore we get started lets introduce both teams...\n')

    def dino_team_intro(self):
        print('Fighting for the DINOSAURS...')
        print(vars(self.herd_1))
        print(self.herd_1.herd[0])

    def robot_team_intro(self):
        print('Fighting for the ROBOTS...')
        print(vars(self.fleet_1))
        print(self.fleet_1.fleet[0].name)
        print(self.fleet_1.fleet[0].weapon.attack_power)

    def battle(self):
        pass

    def dino_turn(self):
        pass

    def robot_turn(self):
        pass

    def show_dino_opponent_options(self):
        pass

    def show_robot_opponent_options(self):
        pass

    def display_winners(self):
        pass