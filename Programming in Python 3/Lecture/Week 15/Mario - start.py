# Mario.py - Game

import random
from tkinter import *

# Lay out our GUI
# parent is Frame
class Application(Frame):
    # class attributes
    WIDTH = 1000
    HEIGHT = 700
    IMAGE_SIZE = 60

    def __init__(self, window):
        # call parent contructor, Frame
        super().__init__(window)
        self.grid()  # displays

        # Canvas - private instance variable
        self.__canvas = Canvas(self, width=Application.WIDTH, height=Application.HEIGHT, bg="black")
        self.__canvas.grid()

        # Images - private instance variables

        # create Mario - private instance variables

        # create enemies - local variables

        # create enemyList - private instance variable

        # bind keyboard
        self.__canvas.bind("<Key>", self.key)
        # focus input on canvas
        self.__canvas.focus_set()

        # kick off the gameLoop
        self.gameLoop()

    # Sets up the key bindings
    def key(self, event):
        #code goes here
        self.__canvas.update()

    # Game Loop
    def gameLoop(self):

        # randomly move our enemies


            # Don't let the enemy go off the screen


        # Check for collisions

        # Don't let Mario go off the screen



        self.after(200, self.gameLoop)


def main():
    root = Tk()
    root.title("Mario Game")
    root.geometry("1000x700")
    app = Application(root)
    root.mainloop()

main()
