from tkinter import *


class MasonsButtons:

	def __init__(self, master):
		frame = Frame(master)
		frame.pack()

		self.printButton = Button(frame, text="print stuff", command=self.printMessage)
		self.printButton.pack(side=LEFT)

		self.quitButton = Button(frame, text="Quit", command=master.destroy)
		self.quitButton.pack(side=LEFT)


	def printMessage(self):
		print("wow, this actually worked")



root = Tk()

mason = MasonsButtons(root)
root.mainloop()