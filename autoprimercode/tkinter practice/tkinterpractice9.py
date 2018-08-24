from tkinter import *

def doNothing():
	print("ok ok I won't")

root = Tk()

# ********* Main Menu **********

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

# ******** Toolbar *********
toolbar = Frame(root, bg="blue")

insertButt = Button(toolbar, text="Insert Image", command=doNothing)
insertButt.pack(side=LEFT, padx=2, pady=2)
printButt = Button(toolbar, text="Print", command=doNothing)
printButt.pack(side=LEFT, padx=2, pady=2)
toolbar.pack(side=TOP, fill=X)

# ********* Status Bar *********

statusBar = Label(root, text="Preparing to do nothing", bd=1, relief=SUNKEN, anchor=W)
statusBar.pack(side=BOTTOM, fill=X)

root.mainloop()


