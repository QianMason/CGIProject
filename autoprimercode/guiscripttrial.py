from tkinter import *
import os
import platform
import subprocess
from tkinter.filedialog import *
import tkinter.messagebox
import primerscript



inputbool = False
outputbool = False
parameterbool = False
inputfp = ""
outputfp = ""
parameterfp = ""
p3filestring = '-p3_settings_file='

def button1():
	entry_1.delete(0,END)
	inputfilepath = askopenfilename()
	entry_1.insert(0, inputfilepath)
	inputfp = inputfilepath
	inputbool = True
	print(inputbool)


def button2():
	entry_2.delete(0,END)
	outputfilepath = asksaveasfilename()
	entry_2.insert(0, outputfilepath)
	outputfp = outputfilepath
	outputbool = True
	print(outputbool)

def button3():
	entry_3.delete(0,END)
	parameterfilepath = askopenfilename()
	entry_3.insert(0, parameterfilepath)
	parameterfp = parameterfilepath
	parameterbool = True
	print(parameterbool)

def buttonstart():
	print("hi")

def doNothing():
	print("do nothing")

def getPrimers():
	#check the booleans if input or output are false, then raise and exception
	print(inputbool, outputbool)
	if (inputbool == False or outputbool == False):
		tkinter.messagebox.showinfo('AUTOPRIMER', 'No input or output filepath detected! Please give an input/output filepath please.')
	else:
		if parameterbool == False:
			outputlocation = '-output=' + outputfp + 'primer3output.txt'
			cmd = ['primer3_core', outputlocation, inputfp]
			subprocess.call(cmd)
		else:
			outputlocation = '-output=' + outputfp + 'primer3output.txt'
			p3filesettings = p3filestring + parameterfilepath
			cmd = ['primer3_core', p3filesettings, outputlocation, inputfp]
			subprocess.call(cmd)


root = Tk()

########## TOP MENU ##########

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

########## ENTRY AREA ##########

entry_1 = Entry(root) #input
entry_2 = Entry(root) #output
entry_3 = Entry(root) #parameters

label_1 = Label(root, text="AUTOPRIMER")
button_1 = Button(root, text="Input Filepath: ", command=button1)
button_2 = Button(root, text="Output Filepath: ", command=button2)
button_3 = Button(root, text="Parameters Filepath: ", command=button3)
button_get = Button(root, text="Get Primers", command=getPrimers)
button_pool = Button(root, text="Pool Primers", command=doNothing)
button_quit = Button(root, text="Quit", command=root.destroy)

label_1.grid(row=0, columnspan=2) #grid doesnt take left right, it takes NSEW directions
button_1.grid(row=1, sticky=E, padx=1, pady=1)
button_2.grid(row=2, sticky=E, padx=1, pady=1)
button_3.grid(row=3, sticky=E, padx=1, pady=1)
button_get.grid(row=4)
button_pool.grid(row=4, column=1)
button_quit.grid(row=4, column=2)

entry_1.grid(row=1, column=1, sticky=W, padx=1, pady=1)
entry_2.grid(row=2, column=1, sticky=W, padx=1, pady=1)
entry_3.grid(row=3, column=1, sticky=W, padx=1, pady=1)

#add submit button which takes entry from all three sources (maybe do file explorer thing)
#add message box that opens up after submit that shows where it was save and to use the command line for the second part



#c = Checkbutton(root, text="Keep me logged in")
#c.grid(columnspan=2)

########## MESSAGE BOX ###########)

answer = tkinter.messagebox.askquestion('AUTOPRIMER', 'Would you like to upload a parameter file?')

if answer == 'yes':
	filename = askopenfilename()
	parameterfp = filename
	entry_3.insert(0, parameterfp)
	paraterbool = True
else:
	tkinter.messagebox.showinfo('AUTOPRIMER', 'You can always upload a file later in the menu.')



root.mainloop()
