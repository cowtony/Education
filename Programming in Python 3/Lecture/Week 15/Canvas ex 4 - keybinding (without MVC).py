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

        #create a rectangle
        self.player = self.canvas.create_rectangle(0,350,50,400, outline = "black", fill = "white")

        #bind keyboard to key function and focus input on canvas
        self.canvas.bind("<Key>", self.key)
        self.canvas.focus_set()



        #kick off our gameLoop event
        self.gameLoop()



    #key event handler
    def key(self, event):
        if event.keysym == "Up" or event.keysym == "w":
            self.canvas.move(self.player,0,-20)
        if event.keysym == "Down" or event.keysym == "s":
            self.canvas.move(self.player,0,20)
        if event.keysym == "Left" or event.keysym == "a":
            self.canvas.move(self.player,-20,0)
        if event.keysym == "Right" or event.keysym == "d":
            self.canvas.move(self.player,20,0)
        self.canvas.update()

    #define our gameLoop event
    def gameLoop(self):
        #comment out auto-move
        # self.canvas.move(self.player,10,0)

        coords = self.canvas.coords(self.player)
        # if self.canvas.coords(self.player)[2] >=1025:
        if coords[2] >=1025:
            self.canvas.move(self.player,-1060,0)
        self.after(20,self.gameLoop)        #called after x milliseconds


def main():
    #create our main window
    root = Tk()
    root.title("Game_Example")
    root.geometry("1000x700")
    app = Application(root)


    root.mainloop()

main()