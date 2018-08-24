import os
import platform
import subprocess
from tkinter import *
from tkinter.filedialog import askopenfilename
import tkinter.messagebox


def doNothing():
	print("do nothing")

def systemChecker():
	if platform.system() == "Windows":
		return "Windows"
	elif platform.system() == "Darwin":
		return "Mac"



def open_file(path):
    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Darwin":
        subprocess.Popen(["open", path])
    else:
        subprocess.Popen(["xdg-open", path])


def loadParameter():
 	if systemChecker() == "Windows":
 		#do something windows related
 		filename = askopenfilename()
 	elif systemChecker() == "Mac":
 		filename = askopenfilename()

 	return filename
