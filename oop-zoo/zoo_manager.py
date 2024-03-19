class Animal:
    # Model of the zoo animals

    def __init__(self, name, species, sound="Animal sound"):
        self.species = species
        self.name = name
        self.sound = sound

    def speak(self):
        return self.sound

    def __str__(self):
        return f"Species: {self.species} Name: {self.name}."


class Mammal(Animal):
    # Model of all the mammals
    def __init__(self, name, species):
        super().__init__(name, species)

    def give_birth(self):
        return f"{self.name} the {self.species} has given birth"


class Aviary():
    def __init__(self, birds=[]):
        self.birds = birds


class Bird(Animal):
    def __init__(self, name, species, wingspan):
        super().__init__(name, species)
        self.wingspan = wingspan


class ReptileEnclosure():
    def __init__(self, reptiles=[]):
        self.reptiles = reptiles


class Reptile(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def bask_in_sun(self):
        return f"{self.name} the {self.species} is basking in the sun"


class Primate(Mammal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def climb_trees(self):
        return f"{self.name} the {self.species} is climbing trees"


class Marsupial(Mammal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def carry_baby(self):
        return f"{self.name} the {self.species} is carrying its baby"


aviary = Aviary([])
print(aviary.birds)
