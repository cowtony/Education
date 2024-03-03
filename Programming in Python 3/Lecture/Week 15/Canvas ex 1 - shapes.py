

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
        self.whiteSquare = self.canvas.create_rectangle(50,600,100,650,fill="white",tag = "white_square")
        self.yellowRectangle = self.canvas.create_rectangle(60,80,400,170,fill="yellow")
        self.redCircle = self.canvas.create_oval(300,300,350,350,fill="red")
        self.greenOval = self.canvas.create_oval(700,500,900,600,fill="green")



def main():
    #create our main window
    root = Tk()
    root.title("Game_Example")
    root.geometry("1000x700")
    app = Application(root)

    root.mainloop()

main()