# Manru Wang
# ITP 115
# Assignment 6
# 3/4/2018
# Description: File Processing

def openCSV(year, outFileName):
    file = open("epaVehicleData" + year + ".csv", "r")
    title = file.readline()

    minMPG = 999
    maxMPG = 0
    maxCAR = list()
    minCAR = list()
    for line in file:
        cells = line.split(',')
        if cells[0].find("VANS") == -1 and cells[0].find("PICKUP") == -1:
            if int(cells[9]) == maxMPG:
                maxCAR.append(cells[1] + " " + cells[2])
            if int(cells[9]) == minMPG:
                minCAR.append(cells[1] + " " + cells[2])
            if int(cells[9]) > maxMPG:
                maxMPG = int(cells[9])
                maxCAR.clear()
                maxCAR.append(cells[1] + " " + cells[2])
            if int(cells[9]) < minMPG:
                minMPG = int(cells[9])
                minCAR.clear()
                minCAR.append(cells[1] + " " + cells[2])

    file.close()

    outFile = open(outFileName, "w")
    outFile.write("EPA Highway MPG Calculator ("+ str(year)+")\n")
    outFile.write("---------------------------------\n")
    outFile.write("Maximum Mileage (highway):"+str(maxMPG))
    for car in maxCAR:
        outFile.write("\t",car)
    outFile.write("Minimum Mileage (highway):"+str(minMPG))
    for car in minCAR:
        outFile.write("\t",car)
    outFile.close()


def main():
    print("Welcome to EPA Mileage Calculator")

    while True:
        year = input("What year would you like to view data for? (2008 or 2009):")
        if year == '2008' or year == '2009':
            break
        else:
            print("*Invalid input, please try again!")

    outFileName = input("Enter the filename to save results to:")

    openCSV(year, outFileName)

    print("Operation Success! Mileage data has been saved to " + outFileName)
    print("Thanks, and have a great day!")


main()