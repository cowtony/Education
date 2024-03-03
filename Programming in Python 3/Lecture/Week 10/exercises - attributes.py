import random

TEMPERAMENTS = ["happy", "nervous", "sleepy", "snuggly"]
class Critter(object):
    def __init__(self, nickname, type, fur):
        print("A new critter has been born!")
        self.name = nickname
        self.hasFur = fur
        self.species = type
        self.temperament = random.choice(TEMPERAMENTS)


def main():
    ginny = Critter("Ginny", "dog",True)
    rex = Critter("Rex", "dog", True)
    don = Critter("Donatello", "turtle", False)

    print("Donatello's temperatment is", don.temperament)

    petList = [ginny, rex, don]
    for pet in petList:
        if pet.hasFur == False:
            print(pet.name, "needs a coat")
        else:
            print(pet.name, "does not need a coat")



main()
