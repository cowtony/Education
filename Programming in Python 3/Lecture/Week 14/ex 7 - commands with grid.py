
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
        self.ent1.grid(column=0, row=0, columnspan=3)

        # Create text entry box
        self.ent2 = Entry(self)
        self.ent2.grid(column=3, row=0, columnspan=3)

        #create a button
        #when clicked, the button will call the printHello method
        # notice how we list the method name WITHOUT parentheses
        self.btn1 = Button(self, text="Display 'Hello'", command=self.actionDisplayHello)
        self.btn1.grid(column=1, row=1)

        #create a button
        #when clicked, the button will call the printText method
        # notice how we list the method name WITHOUT parentheses
        self.btn2 = Button(self, text="Duplicate text!", command=self.actionDuplicateText)
        self.btn2.grid(column=4, row=1)

        #alternate way to BIND functions to buttons
        #create another button
        # when clicked, the button will call the printText method
        self.btn3 = Button(self, text="Remove vowels")
        self.btn3["command"] = self.actionRemoveVowels
        self.btn3.grid(column=0, row=2, columnspan=6, sticky=E)

    # when called, this method will print "Hello" to the console
    def actionDisplayHello(self):
        self.ent2.delete(0,END)
        self.ent2.insert(0,"Hello")


    def actionDuplicateText(self):
        # use get() method to retrieve the content of the
        # entry box (it will always be a string)
        msg = self.ent1.get()

        # insert that text into second entry
        self.ent2.delete(0, END)
        self.ent2.insert(0, msg)


    def actionRemoveVowels(self):
        msg = self.ent1.get()

        msgList = list(msg)
        for i in range(len(msgList) - 1, -1, -1):
            if msgList[i].lower() in "aeiou":
                del msgList[i]
        newMsg = "".join(msgList)

        self.ent2.delete(0, END)
        self.ent2.insert(0, newMsg)



def main():
    root = Tk()
    root.title("Welcome")
    root.geometry("300x300")

    app = Application(root)

    root.mainloop()
main()
