from tkinter import *

root = Tk()

one = Label(root, text="One", bg="red", fg="white")
one.pack()
two = Label(root, text="Two", bg="green", fg="black")
two.pack(fill=X) #by default, its the size of however big it needs to be, fill=X means to fill to the size of the window in the X direction
three = Label(root, text="Three", bg="blue", fg="white")
three.pack(side=LEFT, fill=Y)


root.mainloop()