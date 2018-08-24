from tkinter import *

root = Tk()

def printName(event):
	print("faggot.")

button_1 = Button(root, text="Brian is a?")
button_1.bind("<Button-1>", printName)
button_1.pack(fill=BOTH, expand=True)

root.mainloop()