from dinosaur import Dinosaur

t_rex = ('Tyrannosaurus Flex', 800, 500)

tri = ('Tri-Swole-atops', 1250, 200)

ptero = ('PTerrordactyl', 600, 300)


class Herd:

    def __init__(self):
        self.dinosaurs = []

    def create_herd(self):
        self.dinosaurs.append(t_rex)
        self.dinosaurs.append(tri)
        self.dinosaurs.append(ptero)

