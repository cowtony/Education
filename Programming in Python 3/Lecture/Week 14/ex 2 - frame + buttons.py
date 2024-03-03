from tkinter import *

#create a window
root = Tk()
#change name of window
root.title("Welcome!")
#change size
root.geometry("500x500")



#create Frame to hold other widgets (objects)
app = Frame(root)
#for every widget, you must call grid() to setup widget and make it visible
app.grid()

#create a label widget and add it to the Frame called app
#text color (fg) is white and background (bg) color is magenta (#FF00FF)
lbl1 = Label(app, text="I'm a Label! Yay!", fg="white", bg="#FF00FF")
lbl1.grid()

#create another label widget and add it to the Frame called app
#font is Times, font size is 16 pt, and font style is italic
lbl2 = Label(app, text="I too am also a Label!", font="Times 16 italic")
lbl2.grid()

#create button widget
btn1 = Button(app, text="I'm a button!")
btn1.grid()

# create another button
#text color (fg) color is white and background color (bg) is red
btn2 = Button(app, text="I print the typed text", fg="white", bg="red")
btn2.grid()

#create single-line text box
ent1 = Entry(app)
ent1.grid()

#create another button
#when the button is clicked, the text color is blue and the background is yellow
btn3 = Button(app, text="I print the typed text",  activeforeground="blue", activebackground="yellow",)
btn3.grid()

#create another button
#border (bd) is 10 pixels, height is 5 (LINES), width is 50 (PIXELS)
# and the text is in the top-left corner (anchor)
btn4 = Button(bd=10, height=5, width=50, text="I do nothing!", anchor=NW)
btn4.grid()

#start event loop to listen for user events
root.mainloop()







