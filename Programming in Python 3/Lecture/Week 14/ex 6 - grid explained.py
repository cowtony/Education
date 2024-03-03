from tkinter import *

class Application (Frame):
    def __init__(self, masterWindow):
        #initialize parent object
        super().__init__(masterWindow)
        #call parent function
        self.grid()

        self.btn1 = Button(self, text="row = 0\ncolumn = 0\n")
        self.btn1.grid(row=0, column=0, sticky=N)

        self.btn2 = Button(self, text="row = 0\ncolumn = 1\n")
        self.btn2.grid(row=0, column=1, sticky=E)

        self.btn3 = Button(self, text="row = 0\ncolumn = 2\n")
        self.btn3.grid(row=0, column=2, sticky=S)

        self.btn4 = Button(self, text="row = 1\ncolumn = 0\n")
        self.btn4.grid(row=1, column=0, sticky=W)

        self.btn5 = Button(self, text="row = 1\ncolumn = 1\n")
        self.btn5.grid(row=1, column=1)

        self.btn6 = Button(self, text="row = 1\ncolumn = 2\n")
        self.btn6.grid(row=1, column=2)

        self.btn7 = Button(self, text="row = 2\ncolumn = 0\n")
        self.btn7.grid(row=2, column=0)

        self.btn8 = Button(self, text="row = 2\ncolumn = 2\n")
        self.btn8.grid(row=2, column=1)

        self.btn9 = Button(self, text="row = 2\ncolumn = 2\n")
        self.btn9.grid(row=2, column=2)

        self.btn10 = Button(self, text="row = 3\ncolumn = 0\nspan 2 cols\n")
        self.btn10.grid(row=3, column=0, columnspan=2)

        self.btn11 = Button(self, text="row = 3\ncolumn = 2\n")
        self.btn11.grid(row=3, column=2)




def main():
    root = Tk()
    root.title("Welcome")
    root.geometry("300x300")

    app = Application(root)

    root.mainloop()

main()



