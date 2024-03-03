# Manru Wang
# ITP 115
# Assignment 11
# 4/22/2018
# Description: Part 2: Human Class

from Being import Being

class Human(Being):
    def __init__(self,name,quarts,bloodType):
        super().__init__(name, quarts)
        self.__bloodType=bloodType

    def getBloodType(self):
        return self.__bloodType

    def isAlive(self):
        if self.getQuarts() > 0:
            return True
        else:
            return False

    def __str__(self):
        msg = "Human " + super().getName() + " has " + str(self.getQuarts()) + " quarts of type " + str(self.getBloodType()) + " blood."
        return msg