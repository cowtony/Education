import random

def playAGame():
    num = random.randrange(0, 1001)

    count = 0
    lowerBond = 0
    higherBond = 1000
    while True:
        if count > 10:
            print("Tip: Try to guess a number between", lowerBond, "to", higherBond)
        else:
            print("Guess a number between 0 and 1000")
        guess = input("")
        var = int(guess)

        count += 1

        if var < 0 or var > 1000:
            print("Please enter a valid number between 0 and 1000")
            continue

        if var == num:
            print("You are correct")
            break
        elif var < num:
            print("Try higher please")
            lowerBond = var + 1
        elif var > num:
            print("Try lower please")
            higherBond = var - 1

def playAgain():
    again = input("Do you want to play again (Y/N)? ")
    if again == "n":
        print("Game over, goodbye ")
        return False
    if again == "N":
        print("type lower case n")


def main():
    while True:
        playAGame()
        if playAgain() == False:
            break


main()
