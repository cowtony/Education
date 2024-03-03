# Manru Wang
# ITP 115
# Assignment 11
# 4/22/2018
# Description: Part 4: Main

from Human import Human
from Vampire import Vampire

def printHuman(humanList):
    for i in range(len(humanList)):
        print(str(i), ") "+str(humanList[i]))

def performFeeding(humanList,vamp):
    indexNum=int(input("Please select a human from the list:"))
    human=humanList[indexNum]

    if indexNum<0 or indexNum>3:
        print("Error, please try again.")

    if human.isAlive() is True and vamp.isStuffed() is False:
        vamp.suckBlood(human)
        print(human)
        print(vamp)
    elif vamp.isStuffed() is True:
        print(vamp)
        print(vamp.getName()+" cannot suck any more blood!")

    elif human.isAlive() is False:
        print(human.getName() + "is dead. Cannot suck blood!")
        print(vamp)

def main():

    h1 = Human("Eric Brooks", 5, "A-")
    h2 = Human("Mina Harker", 7, "O+")
    h3 = Human("Louis de Pointe du Lac", 4, "O+")
    h4 = Human("Annie Sawyer", 3, "B-")

    humanList=[h1,h2,h3,h4]

    askName = input("Please enter your name:")
    askAnimal = input("Please enter an animal: ")

    v1 = Vampire(askName, 0, askAnimal)

    while True:
        choice = input("\nMenu:\n1 --> Print All Humans\n2 --> Suck Blood\n-1 --> Quit\nEnter your choice:")
        if choice =="1":
            print("")
            printHuman(humanList)

        elif choice=="2":
            print("")
            printHuman(humanList)
            performFeeding(humanList, v1)

        elif choice=="-1":
            print(askName,"transformed back into a",askAnimal)
            break
        else:
            print("Error, please try again!")

main()


