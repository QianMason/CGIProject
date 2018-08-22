from tkinter import *

def doNothing():
	print("ok ok I won't")

root = Tk()


menu = Menu(root) #menu object
root.config(menu=menu)

fileMenu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New Project...", command=doNothing)
fileMenu.add_command(label="New...", command=doNothing)
fileMenu.add_separator()
fileMenu.add_command(label="Quit", command=root.destroy)

editMenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=doNothing)


frame = Frame(root, width=300, height=250)
frame.pack()

root.mainloop()


