class Dog:

    animal_kind = "canine" #class variable

    def bark(self):
        self.animal_kind #method variable inside the class
        return "woof"

    def eat(self, eat):
        self.eat = eat
        return "nom nom nom ..."

fido = Dog() # Initialising our class/ creating an object
lucy = Dog()
print(lucy.animal_kind)
print(fido.animal_kind)
print(fido.bark())

fido.animal_kind = "fish"
print(fido.animal_kind)