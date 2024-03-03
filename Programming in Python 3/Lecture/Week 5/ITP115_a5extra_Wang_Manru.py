# Manru Wang
# ITP 115
# Assignment 5 Extra Credit
# 2/18/2018
# Description: Tic Tac Toe - Extra Credit

import TicTacToeHelper
import random

def isValidMove(boardList, spot):
    # If spot out of range [0,8]
    if spot < 0 or spot > 8:
        return False
    # If spot is taken
    elif boardList[spot] == "x" or boardList[spot] == "o":
        return False
    # If spot is open
    elif int(boardList[spot]) == spot:  # If spot is written the same number as index
        return True
    else:
        return False


def updateBoard(boardList, spot, playerLetter):
    #Takes the current board lsit and places the player's letter in the specified spot on the board
    if playerLetter == 'x' or playerLetter == 'o':
        boardList[spot] = playerLetter


def playGame():
    boardList = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
    numberOfMove = 0

    printPrettyBoard(boardList)

    vscomputer = input("Play with computer?(y/n)")
    player = input("Which player to begin with?")

    while True:

        if vscomputer=="y"and numberOfMove % 2 == 1:
            while True:
                spot=random.randrange(9)
                if isValidMove(boardList, spot) == True:
                    break

        else:
            while True:
                spot = int(input("Player " + player + " pick a spot: "))
                if isValidMove(boardList, spot) == True:
                    break
                else:
                    print("Invalid move, please try again.")

        updateBoard(boardList, spot, player)
        numberOfMove = numberOfMove + 1
        printPrettyBoard(boardList)

        result = TicTacToeHelper.checkForWinner(boardList, numberOfMove)

        if result == "s":
            print("Game Over!")
            print("Stalemate reached!")
            break
        elif result == "x" or result == "o":
            print("Game Over!")
            print("Player", player, " is the winner!")
            break

        #player take turns
        if player == "x":
            player = "o"
        else:
            player = "x"

def printPrettyBoard(boardList):
    print()
    counter = 0
    for i in range(3):
        for j in range(3):
            if j<2:
                print(boardList[counter],"|", end="")
            else:
                print(boardList[counter], end="")
            counter += 1
        if i<2:
            print("\n---------",end="")
        print()


def main():
    print("Welcome to Tic Tac Toe!")


    while True:
        playGame()
        anotherRound = input("Would you like to play another round? (y/n): ")
        if anotherRound == "y":
            continue
        elif anotherRound == "n":
            print("Goodbye!")
            break


main()