from tkinter import *
import os
import platform
import subprocess

root = Tk()


def doNothing():
	print("do nothing")


def open_file(path):
    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Darwin":
        subprocess.Popen(["open", path])
    else:
        subprocess.Popen(["xdg-open", path])


def entry1():
 	e1 = entry_1.get()
 	print(e1)

def entry2():
 	e2 = entry_2.get()
 	print(e2)

def entry3():
 	e3 = entry_3.get()
 	print(e3) 	


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

label_1 = Label(root, text="AUTOPRIMER")
label_2 = Button(root, text="Input Filepath: ", command=entry1)
label_3 = Button(root, text="Output Filepath: ", command=entry2)
label_4 = Button(root, text="Parameters Filepath: ", command=entry3)


entry_1 = Entry(root)
entry_2 = Entry(root, show='*')
entry_3 = Entry(root)


label_1.grid(row=0, columnspan=2) #grid doesnt take left right, it takes NSEW directions
label_2.grid(row=1, sticky=E, padx=1, pady=1)
label_3.grid(row=2, sticky=E, padx=1, pady=1)
label_4.grid(row=3, sticky=E, padx=1, pady=1)

entry_1.grid(row=1, column=1, sticky=W, padx=1, pady=1)
entry_2.grid(row=2, column=1, sticky=W, padx=1, pady=1)
entry_3.grid(row=3, column=1, sticky=W, padx=1, pady=1)


#add submit button which takes entry from all three sources (maybe do file explorer thing)
#add message box that opens up after submit that shows where it was save and to use the command line for the second part



#c = Checkbutton(root, text="Keep me logged in")
#c.grid(columnspan=2)





root.mainloop()
