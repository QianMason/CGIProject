import subprocess
import tkinter as tk
from tkinter.filedialog import *
import tkinter.messagebox

class AUTOPRIMER(tk.Tk):

	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)

		self.input = ""
		self.output = ""
		self.param = ""
		self.inputbool = False
		self.outputbool = False
		self.parambool = False
		self.p3filestring = '-p3_settings_file='

	entry_1 = tk.Entry(self) #input
	entry_2 = tk.Entry(self) #output
	entry_3 = tk.Entry(self) #parameters

	label_1 = tk.Label(self, text="AUTOPRIMER")
	button_1 = tk.Button(self, text="Input Filepath: ", command=button1)
	button_2 = tk.Button(self, text="Output Filepath: ", command=button2)
	button_3 = tk.Button(self, text="Parameters Filepath: ", command=button3)
	button_get = tk.Button(self, text="Get Primers", command=getPrimers)
	button_pool = tk.Button(self, text="Pool Primers", command=doNothing)
	button_quit = tk.Button(self, text="Quit", command=self.destroy)

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





	@classmethod
	def getPrimers(cls):
		if inputbool == False or outputbool == False:
			return #do something that tkinter can pick up on
		else:
			if parameterbool == False:
				outputlocation = '-output=' + outputfp + 'primer3output.txt'
				cmd = ['primer3_core', outputlocation, input]
				subprocess.call(cmd)
			else: #parameters present
				outputlocation = '-output=' + output + 'primer3output.txt'
				p3filesettings = self.p3filestring + param
				cmd = ['primer3_core', p3filesettings, outputlocation, input]
				subprocess.call(cmd)

	def PrimerParser(filepath):
		#takeoutput of primer3 run and parse for primers
		#ask user to indicate number of primers they set or you can reuse the number the user set earlier
		count = 0
		primerpairs = {}
		leftprimers = []
		rightprimers = []

		with open(filepath, 'r') as primer_file:

			lines = primer_file.readlines()
			for line in lines:
				if (line.startswith('PRIMER_LEFT_0_SEQUENCE')):
					leftprimers.append(line.split('=')[1])
				if (line.startswith('PRIMER_RIGHT_0_SEQUENCE')):
					rightprimers.append(line.split('=')[1])
				if (line.startswith('PRIMER_PAIR_NUM_RETURNED=0')):
					print('primer pair not found for some sequence(s), please check output file')

		#right here i may want to add functionality for the user to upload ane existing sheet to append more primers to?
		with open(filepath + 'primerlist.txt', 'w+') as primer_output:
			for i in range(len(leftprimers)):
				primer_output.write('>' + 'primer' + str(i) + '-F' + '\n')
				primer_output.write(leftprimers[i])
				primer_output.write('>' + 'primer' + str(i) + '-R' + '\n')
				primer_output.write(rightprimers[i])


	def setInput(self, value):
		self.input = value
	def setOutput(self, value):
		self.output = value
	def setParam(self, value):
		self.param = value
	def setinputbool(self, value):
		self.inputbool = value
	def button1(ifp):
		entry_1.delete(0,END)
		ifp = askopenfilename()
		entry_1.insert(0, ifp)
		inputbool = True
		print("input bool value is: " + str(inputbool))
	def button2(ofp):
		entry_2.delete(0,END)
		ofp = asksaveasfilename()
		entry_2.insert(0, ofp)
		outputbool = True
		print("output bool value is: " + str(outputbool))
	def button3(pfp):
		entry_3.delete(0,END)
		pfp = askopenfilename()
		entry_3.insert(0, parameterfilepath)
		parameterbool = True
		print("parameter bool value is: " + str(parameterbool))

def main():
	autoprimer = AUTOPRIMER()
	autoprimer.mainloop()
