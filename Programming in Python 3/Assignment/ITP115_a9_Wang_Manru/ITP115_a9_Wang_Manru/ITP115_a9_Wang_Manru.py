# Manru Wang
# ITP 115
# Assignment 9
# 4/1/2018
# Description: OOP (Animal Daycare)

class Animal(object):
    hunger=0
    happiness=0
    health=0
    energy=0
    age=0
    name=""
    species=""

    def __init__(self,modeHunger,modeHappiness,modeHealth,modeEnergy,modeAge,modeName,modeSpecies):
        if modeHunger<0:
            modeHunger=0
        if modeHunger>100:
            modeHunger=100
        if modeHappiness<0:
            modeHappiness=0
        if modeHappiness>100:
            modeHappiness=100
        if modeHealth<0:
            modeHealth=0
        if modeHealth>100:
            modeHealth=100
        if modeEnergy<0:
            modeEnergy=0
        if modeEnergy>100:
            modeEnergy=100

        self.hunger=modeHunger
        self.happiness=modeHappiness
        self.health=modeHealth
        self.energy=modeEnergy
        self.age=modeAge
        self.name=modeName
        self.species=modeSpecies

    def play(self):
        self.happiness+=10
        if self.happiness>100:
            self.happiness=100
        self.hunger+=5
        if self.hunger>100:
            self.hunger=100

    def feed(self):
        self.hunger-=10
        if self.hunger<0:
            self.hunger=0

    def giveMedicine(self):
        self.happiness-=20
        if self.happiness<0:
            self.happiness=0
        self.health+=20
        if self.health>100:
            self.health=100

    def sleep(self):
        self.energy+=20
        if self.energy>100:
            self.energy=100
        self.age+=1

    def __str__(self):
        msg = "Name: "+self.name+self.species
        msg += "\nHealth: "+str(self.health)
        msg += "\nHappiness: "+str(self.happiness)
        msg += "\nHunger: "+str(self.hunger)
        msg += "\nEnergy: "+str(self.energy)
        msg += "\nAge: "+str(self.age)
        return msg



def loadAnimals(csvName):
    file=open(csvName,"r")
    animalList=[]
    for line in file:
        cell=line.split(",")
        animal=Animal(int(cell[0]),int(cell[1]),int(cell[2]),int(cell[3]),int(cell[4]),cell[5],cell[6])

        animalList.append(animal)
    file.close()
    return animalList



def displayMenu():
    print("1) Play\n2) Feed\n3) Give Medicine\n4) Sleep\n5) Print an Animal's stats\n6) View All Animals\n7) Exit")

def selectAnimal(animalObject):
    i=1
    for animal in animalObject:
        print(str(i)+")"+animal.name+" the "+animal.species)
        i+=1
    while True:
        choice=int(input("Please select an animal from the list (enter the 1-"+str(len(animalObject))+":)"))
        if choice>0 and choice<len(animalObject)+1:
            return animalObject[choice-1]
        else:
            print("Invalid input, please try again!")



def main():
    print("Welcome to the Animal Daycare! Here is what we can do:")
    animalObject=loadAnimals("animals.csv")

    while True:
        displayMenu()
        answer=int(input("\nPlease make a selection:"))
        if answer>0 and answer<6:
            options=selectAnimal(animalObject)
            if answer==1:
                options.play()
                print("You played with",options.name,"the",options.species)
            if answer==2:
                options.feed()
                print("You fed", options.name, "the", options.species)
            if answer==3:
                options.giveMedicine()
                print("You gave", options.name, "the", options.species+"some medicine!")
            if answer==4:
                options.sleep()
                print(options.name, "the", options.species+"took a nap!")
            if answer==5:
                print(options)
        elif answer==6:
            for animal in animalObject:
                print(animal)
                print("***************************")
        elif answer==7:
            print("Goodbye!")
        else:
            print("*Invalid input, please try again!*\n")



main()




