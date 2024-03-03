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
        self.gui_rect = self.canvas.create_rectangle(0,350,50,400, outline = "black", fill = "white")


        #kick off our gameLoop event
        self.gameLoop()



    #define our gameLoop event
    def gameLoop(self):
        self.canvas.move(self.gui_rect,10,0)  #define what you want to do here
        self.after(20, self.gameLoop)        #called after x milliseconds



def main():
    #create our main window
    root = Tk()
    root.title("Game_Example")
    root.geometry("1000x700")
    app = Application(root)

    root.mainloop()

main()