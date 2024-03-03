from tkinter import *

# In the previous example, we created a Frame to store all our widgets.
# Now, we are creating a new class which is derived from the Frame class
# so that we can simplify our code
class Application (Frame):
    def __init__(self, masterWindow):
        #initialize parent object
        super().__init__(masterWindow)

        #since this class is derived from Frame,
        # we need to call grid()
        self.grid()

        # we are adding all widgets as INSTANCE variables of the
        # class
        self.lbl1 = Label(self, text="I'm a label")
        self.lbl1.grid()

        self.lbl2 = Label(self, text="I'm a label2", fg="red")
        self.lbl2.grid()

        self.lbl3 = Label(self, text="I'm a label3", fg="blue")
        self.lbl3.grid()

        self.ent1 = Entry(self)
        self.ent1.grid()

        self.btn1 = Button(self, text="I do nothing!")
        self.btn1.grid()

        self.btn2 = Button(self, text="I say hello!")
        self.btn2.grid()

        self.btn3 = Button(self, text="I say goodbye!")
        self.btn3.grid()




def main():
    root = Tk()
    root.title("Welcome")
    root.geometry("200x200")

    #instead of creating a Frame, we are creating one of our
    # new, inherited Application objects
    app = Application(root)

    root.mainloop()
main()
