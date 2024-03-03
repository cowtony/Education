# Given a tic, tac, toe board determine if there is a winner
# Function inputs:
#     board_list: an array of 9 strings representing the tic tac toe board
#     move_counter: an integer representing the number of moves that have been made
# Returns a string:
#     'x' if x won
#     'o' if o won
#     'n' if no one wins
#     's' if there is a stalemate
def checkForWinner(board_list, move_counter):
    j = 0
    for i in range(0, 9, 3):
        # Check for 3 in a row
        if board_list[i] == board_list[i+1] == board_list[i+2]:
            return board_list[i]

        # Check for 3 in a column
        elif board_list[j] == board_list[j+3] == board_list[j+6]:
            return board_list[j]

        # Check the diagonal from the top left to the bottom right
        elif board_list[0] == board_list[4] == board_list[8]:
            return board_list[0]

        # Check the diagonal from top right to bottom left
        elif board_list[2] == board_list[4] == board_list[6]:
            return board_list[2]
        j += 1

    # If winner was not found and board is completely filled up, return stalemate
    if move_counter > 8:
        return "s"

    # Otherwise, 3 in a row anywhere on the board
    return "n"


# Print out the tic tac toe board
# Input: list representing the tic tac toe board
# Return value: none
def printUglyBoard(board_list):
    print()
    counter = 0
    for i in range(3):
        for j in range(3):
            print(board_list[counter], end="  ")
            counter += 1
        print()


# Return value: True or False
def isValidMove(boardList, spot):
    # If spot out of range [0,8]

    # If spot is taken

    # If spot is open

# Takes the current board list and places the player's letter in the specified spot on the board
# Return: nothing
def updateBoard(boardList, spot, playerLetter):


# Return: nothing
def playGame():
    boardList = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
    numberOfMove = 0

    # keep programming here

def main():
    print("Welcome to Tic Tac Toe!")
    # play the game by calling playGame and ask user for play again


main()