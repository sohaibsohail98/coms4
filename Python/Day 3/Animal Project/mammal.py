from animal import Animal

class Mammal(Animal):
    def __init__(self, alive, hungry = True, sleeping = False, breathing = True, species, prey, predator, breathing = True):
        super().__init__(alive, hungry = True, sleeping = False, breathing = True)

    self.species = species
    self.prey = prey
    self.predator = predator
    self.breathing = breathing
