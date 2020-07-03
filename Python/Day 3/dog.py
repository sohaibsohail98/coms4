class Dog:
    animal_kind = "canine" #Class variable

    def __init__(self, name, colour): #initialisation
        self.name = name
        self.colour = colour

    def bark(self):
        return "woof woof"

    def sleep(self):
        return "snooring"

    def breath(self):
        return "breathing"

    def run(self):
        return "running"

    def eat(self):
        return "eating"

#These are functions for each type of dog activity occuring.

fido = Dog("canine", "white") #creating an object of our class
print(fido.colour) #printing an attribute of our class

lucy = Dog("lucky", "brown")
print(lucy.colour)



#create a functions inside for sleep, breath, run,eat

