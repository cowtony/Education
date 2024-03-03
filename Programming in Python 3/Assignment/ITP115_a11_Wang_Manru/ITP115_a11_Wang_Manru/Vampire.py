# Manru Wang
# ITP 115
# Assignment 11
# 4/22/2018
# Description: Part 3: Vampire Class

from Being import Being

class Vampire(Being):
    MAX_BLOOD=5
    HUNGER_LEVELS=["starving","hangry","hungry","content","full","stuffed"]

    def __init__(self,name,quarts,animalform):
        super().__init__(name, quarts)
        self.__animalForm=animalform

    def getAnimalForm(self):
        return self.__animalForm

    def getHunger(self):
        hungerLevel= Vampire.HUNGER_LEVELS[self.getQuarts()]
        return hungerLevel

    def isStuffed(self):
        if self.getQuarts()==Vampire.MAX_BLOOD:
            return True
        else:
            return False

    def suckBlood(self,human):
        human.decreaseQuarts()
        self.increaseQuarts()

    def __str__(self):
        msg = self.getName() + " is " + self.getHunger()
        return msg
