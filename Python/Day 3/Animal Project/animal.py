class Animal:

    def __init__(self, alive, hungry = True, sleeping = False, breathing = True):
        self.alive = alive
        self.hungry = hungry
        self.sleeping = sleeping
        self.breathing = breathing

    def condition(self):
        if self.alive == True: # If the animal is still alive, print the statement
            print("The animal is still alive")
        elif self.alive == False:
            print("The animal is dead now, RIP.")

    def eating(self):
        if self.hungry == True:
            print("I need food!")
        elif self.hungry == False:
            print("I don't need food!")

    def breath(self):
        if self.breathing == True:
            print("Good to know that you are breathing")
        elif self.breathing == False:
            print("Say hi to god from me!")

    def hiberate(self):
        if self.sleeping == True:
            print("Sleep tight! Wake up tomorrow fresh")
        elif self.sleeping == False:
            print("Get up, and go reproduce!")


Lion = Animal("yes", hungry = False, sleeping = False, breathing = True)

Lion.condition()
Lion.eating()
Lion.breath()
Lion.hiberate()
