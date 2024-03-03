
from tkinter import *

# In the previous example, we created a Frame to store all our widgets.
# Now, we are creating a new class which is derived from the Frame class
# so that we can simplify our code
class Application (Frame):
    def __init__(self, masterWindow):
        #initialize parent object
        super().__init__(masterWindow)
        #call parent function
        self.grid()

        #Create text entry box
        self.ent1 = Entry(self)
        self.ent1.grid(column=0, row=0, sticky=W)

        # Create text entry box
        self.ent2 = Entry(self)
        self.ent2.grid(column=1, row=0, sticky=W)

        #Radiobutton
        #create a special variable to store the VALUE of these radio buttons
        self.stringVarCreditCard = StringVar()
        self.stringVarCreditCard.set("v")

        self.radioCreditCardVisa = Radiobutton(self, text="Visa", value="v", variable=self.stringVarCreditCard)
        self.radioCreditCardVisa.grid(row=2, column=0)
        self.radioCreditCardMasterCard = Radiobutton(self, text="Master Card", value="mc", variable=self.stringVarCreditCard)
        self.radioCreditCardMasterCard.grid(row=2, column=1)


        #Checkbutton
        #make check button variable
        self.booleanVarTerms = BooleanVar()

        self.checkTerms = Checkbutton(self, text="Accept terms and conditions? ", variable=self.booleanVarTerms)
        self.checkTerms.grid(row=4, column=0)

        self.btn4 = Button(self, text="Results", command=self.actionShowResults)
        self.btn4.grid(column=0, row=5)

    def actionShowResults(self):
        # read the value of the radiobutton
        msg = self.stringVarCreditCard.get()
        self.ent1.delete(0, END)
        self.ent1.insert(0, msg)

        # read the value of the check box
        answer = self.booleanVarTerms.get()
        self.ent2.delete(0, END)
        if answer == True:
            self.ent2.insert(0, "Accepted!")
        else:
            self.ent2.insert(0, "Did NOT accept")


def main():
    root = Tk()
    root.title("Welcome")
    root.geometry("500x300")

    app = Application(root)

    root.mainloop()
main()
