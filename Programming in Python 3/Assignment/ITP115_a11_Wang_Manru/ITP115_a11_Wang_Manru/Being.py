# Manru Wang
# ITP 115
# Assignment 11
# 4/22/2018
# Description: Part 1: Being Class

class Being(object):
    def __init__(self,name,quarts):
        self.__name=name
        self.__quarts=int(quarts)

    def getName(self):
        return self.__name

    def getQuarts(self):
        return self.__quarts

    def setName(self, newName):
        self.__name = newName

    def setQuarts(self, newQuarts):
        self.__quarts = newQuarts

    def increaseQuarts(self):
        self.__quarts += 1

    def decreaseQuarts(self):
        self.__quarts -= 1


