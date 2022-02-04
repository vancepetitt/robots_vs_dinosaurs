from dinosaur import Dinosaur

class Herd:

    def __init__(self):
        self.herd = []
        self.create_herd()

    def create_herd(self):
        #Dinosaurs
                
        dinosaur_2 = Dinosaur('Tyrannosaurus Flex', 800, 500, 'Watch out for his bite! He might skip arm day, but those teeth of his pack a HUGE punch! With decent size and a devastating bite attack, T-Flex is a force to be reckoned with!')

        dinosaur_3 = Dinosaur('Tri-Swole-atops', 1250, 150, 'A cretaceous powerhouse! This beefy dino can shrug off most hits without breaking a sweat. His horns will keep attackers at bay, but his charges are easily avoidable.')

        dinosaur_1 = Dinosaur('PTerrordactyl', 600, 300, 'Keep your head down! While she isnt as beefy as the other dinos, this aerial menace never misses with her birds-eye view of the battlefield!')

              
        self.herd.append(dinosaur_1)
        self.herd.append(dinosaur_2)
        self.herd.append(dinosaur_3)
