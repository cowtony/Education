# Manru Wang
# ITP 115
# Assignment 10
# 4/8/2018
# Description: OOP Part 2 (Superheroes)

class Superhero(object):
    def __init__(self,modeName,modeType,modeAttack):
        self.__name=modeName
        self.__type=modeType
        self.__attack=modeAttack
        self.__health=100

    def getName(self):
        return self.__name

    def getAttack(self):
        return self.__attack

    def getHealth(self):
        return self.__health

    def getType(self):
        return self.__type

    def loseHealth(self,attack):
        self.__health -= attack

    def isDead(self):
        if self.__health<=0:
            return True
        else:
            return False

    def __str__(self):
        msg=self.__name+" the "+self.__type+" has "+str(self.__attack)+" attack point and currently has "+str(self.__health)+" points of health."
        return msg
