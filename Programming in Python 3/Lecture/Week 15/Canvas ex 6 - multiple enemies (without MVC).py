from tkinter import *


class Application(Frame):
    def __init__(self, root):
        #call PARENT constructor, AKA FRAME
        super().__init__(root)
        #Application inherits from Frame
        #Frame needs to call grid() to appear on the screen
        #therefore, Application also has to call grid
        self.grid()

        #create our canvas and grid it to window
        self.canvas = Canvas (self, width = 1000, height = 700, bg = "black")
        self.canvas.grid()

        #create our frontend and backend rectangle
        self.player = self.canvas.create_rectangle(0,350,50,400, outline = "black", fill = "white", tag = "player")

        #create an enemy
        enemy1 = self.canvas.create_rectangle(500,350,550,400, outline = "black", fill = "red", tag = "enemy")
        enemy2 = self.canvas.create_rectangle(300,150,350,200, outline = "black", fill = "red")
        enemy3 = self.canvas.create_rectangle(750,500,800,550, outline = "black", fill = "red")

        #add enemy to a list to prep collision checking
        self.enemyList = []
        self.enemyList.append(enemy1)
        self.enemyList.append(enemy2)
        self.enemyList.append(enemy3)



        #bind keyboard to key function and focus input on canvas
        self.canvas.bind("<Key>", self.key)
        self.canvas.focus_set()

        #kick off our gameLoop event
        self.gameLoop()


    #define our key event handler
    def key(self, event):
        if event.keysym == "Up" or event.keysym == "w":
            self.canvas.move(self.player,0,-20)
        elif event.keysym == "Down" or event.keysym == "s":
            self.canvas.move(self.player,0,20)
        elif event.keysym == "Left" or event.keysym == "a":
            self.canvas.move(self.player,-20,0)
        elif event.keysym == "Right" or event.keysym == "d":
            self.canvas.move(self.player,20,0)
        self.canvas.update()


    #define our gameLoop
    def gameLoop(self):
        #say what we want out gameLoop to do
        #check for collisions - find_overlapping returns a tuple of id's
        coords = self.canvas.bbox(self.player)
        collisions = self.canvas.find_overlapping(coords[0],
                                                  coords[1],
                                                  coords[2],
                                                  coords[3])
        for collision in collisions:
            if collision in self.enemyList:
                self.canvas.delete(collision)




        #loop after x many milliseconds
        self.after(20,self.gameLoop)



def main():
    #create our main window
    root = Tk()
    root.title("Game_Example")
    root.geometry("1000x700")
    app = Application(root)

    root.mainloop()

main()

