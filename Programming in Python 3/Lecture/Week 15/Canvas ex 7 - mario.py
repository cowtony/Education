from tkinter import *


class Application(Frame):
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 700
    PLAYER_WIDTH = 50
    PLAYER_HEIGHT = 50

    def __init__(self, root):
        # call PARENT constructor, AKA FRAME
        super().__init__(root)
        self.goombaMovementCounter = 1
        # Application inherits from Frame
        # Frame needs to call grid() to appear on the screen
        # therefore, Application also has to call grid
        self.grid()

        # create our canvas and grid it to window
        self.canvas = Canvas(self, width=Application.SCREEN_WIDTH, height=Application.SCREEN_HEIGHT, bg="black")
        self.canvas.grid()

        self.imageMario = PhotoImage(file="mario.gif")
        self.imageGoomba = PhotoImage(file="goomba.gif")
        # create our frontend and backend rectangle
        # self.player = self.canvas.create_rectangle(0,350,50,400, outline = "black", fill = "white", tag = "player")
        self.player = self.canvas.create_image(Application.PLAYER_WIDTH, Application.SCREEN_HEIGHT / 2,
                                               image=self.imageMario)

        # create an enemy
        enemy1 = self.canvas.create_image(500, 350, image=self.imageGoomba)
        enemy2 = self.canvas.create_image(300, 150, image=self.imageGoomba)
        enemy3 = self.canvas.create_image(750, 500, image=self.imageGoomba)
        # enemy1 = self.canvas.create_rectangle(500,350,550,400, outline = "black", fill = "red", tag = "enemy")
        # enemy2 = self.canvas.create_rectangle(300,150,350,200, outline = "black", fill = "green")
        # enemy3 = self.canvas.create_rectangle(750,500,800,550, outline = "black", fill = "blue")

        # add enemy to a list to prep collision checking
        self.enemyList = []
        self.enemyList.append(enemy1)
        self.enemyList.append(enemy2)
        self.enemyList.append(enemy3)

        # bind keyboard to key function and focus input on canvas
        self.canvas.bind("<Key>", self.key)
        self.canvas.focus_set()

        # kick off our gameLoop event
        self.gameLoop()

    # define our key event handler
    def key(self, event):
        if event.keysym == "Up" or event.keysym == "w":
            self.canvas.move(self.player, 0, -20)
        elif event.keysym == "Down" or event.keysym == "s":
            self.canvas.move(self.player, 0, 20)
        elif event.keysym == "Left" or event.keysym == "a":
            self.canvas.move(self.player, -20, 0)
        elif event.keysym == "Right" or event.keysym == "d":
            self.canvas.move(self.player, 20, 0)
        self.canvas.update()

    # define our gameLoop
    def gameLoop(self):

        # say what we want out gameLoop to do
        # check for collisions - find_overlapping returns a tuple of id's
        # coords = self.canvas.coords(self.player)
        coords = self.canvas.bbox(self.player)
        collisions = self.canvas.find_overlapping(coords[0],
                                                  coords[1],
                                                  coords[2],
                                                  coords[3])

        self.goombaMovementCounter += 1
        # print("player coords: ", coords[3], "self.enemies[0]:", self.canvas.bbox(self.enemyList[0])[1])
        # print("player coords: ", coords, "self.enemies[0]:", self.canvas.bbox(self.enemyList[0]))

        for enemy in self.enemyList:
            moveX = (self.goombaMovementCounter % 51) - 25
            self.canvas.move(enemy, moveX, 0)

        for collision in collisions:
            if collision in self.enemyList:
                # if coords[3] <= self.canvas.bbox(collision)[1]:
                self.canvas.delete(collision)

        if coords[0] >= 1000:
            self.canvas.move(self.player,-1000,0)
        elif coords[2] <= 0:
            self.canvas.move(self.player,1060,0)
        elif coords[1] >= 700:
            self.canvas.move(self.player,0,-700)
        elif coords[3] <= 0:
            self.canvas.move(self.player,0,700)

        # loop after x many milliseconds
        self.after(100, self.gameLoop)


def main():
    # create our main window
    root = Tk()
    root.title("Game_Example")
    root.geometry("1000x700")
    app = Application(root)

    root.mainloop()


main()
