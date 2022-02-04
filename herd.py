from cgi import test
from dinosaur import Dinosaur

class Herd:

    def __init__(self):
        self.herd = []
        self.create_herd()

    def create_herd(self):
        #Dinosaurs
                
        dinosaur_1 = ('Tyrannosaurus Flex', 800, 500)

        dinosaur_2 = ('Tri-Swole-atops', 1250, 150)

        dinosaur_3 = ('PTerrordactyl', 600, 300)

              
        self.herd.append(dinosaur_1)
        self.herd.append(dinosaur_2)
        self.herd.append(dinosaur_3)
