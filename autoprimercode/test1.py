import subprocess
from tkinter import *
from tkinter.filedialog import *
import tkinter.messagebox

class AUTOPRIMER:

	def __init__(self, master):

		def doNothing():
			print("Do nothing")
		def setInput(value):
			self.input = value
		def setOutput(value):
			self.output = value
		def setParam(value):
			self.param = value
		def setInputbool(value):
			self.inputbool = value
		def setOutputbool(value):
			self.outputbool = value
		def setParameterbool(value):
			self.parameterbool = value
		def button1():
			entry_1.delete(0,END)
			ifp = askopenfilename()
			setInput(ifp)
			entry_1.insert(0, ifp)
			setInputbool(True)
			print("input bool value is: " + str(self.inputbool))
		def button2():
			entry_2.delete(0,END)
			ofp = asksaveasfilename()
			setOutput(ofp)
			entry_2.insert(0, ofp)
			setOutputbool(True)
			print("output bool value is: " + str(self.outputbool))
		def button3():
			entry_3.delete(0,END)
			pfp = askopenfilename()
			entry_3.insert(0, pfp)
			setParameterbool(True)
			print("parameter bool value is: " + str(self.parameterbool))
		def getPrimers():

			print(self.inputbool, self.outputbool)
			if self.inputbool == False or self.outputbool == False:
				pass
			else:
				if self.parameterbool == False:
					outputlocation = '-output=' + self.output + 'primer3output.txt'
					cmd = ['primer3_core', outputlocation, self.input]
					subprocess.call(cmd)
				else: #parameters present
					outputlocation = '-output=' + self.output + 'primer3output.txt'
					p3filesettings = self.p3filestring + self.param
					cmd = ['primer3_core', p3filesettings, outputlocation, self.input]
					subprocess.call(cmd)

		def PrimerParser():
			#takeoutput of primer3 run and parse for primers
			#ask user to indicate number of primers they set or you can reuse the number the user set earlier
			count = 0
			primerpairs = {}
			leftprimers = []
			rightprimers = []
			filepath = self.output + 'primer3output.txt'
			missingprimerbool = False
			with open(filepath, 'r') as primer_file:

				lines = primer_file.readlines()
				for line in lines:
					if (line.startswith('PRIMER_LEFT_0_SEQUENCE')):
						leftprimers.append(line.split('=')[1])
					if (line.startswith('PRIMER_RIGHT_0_SEQUENCE')):
						rightprimers.append(line.split('=')[1])
					if (line.startswith('PRIMER_PAIR_NUM_RETURNED=0') and missingprimerbool == False):
						#print('primer pair not found for some sequence(s), please check output file')
						missingprimerbool = True
						tkinter.messagebox.showinfo('AUTOPRIMER', 'Primer pair not found for some sequence(s), please check output file')

			#right here i may want to add functionality for the user to upload ane existing sheet to append more primers to?
			with open(filepath + 'primerlist.txt', 'w+') as primer_output:
				for i in range(len(leftprimers)):
					primer_output.write('>' + 'primer' + str(i) + '-F' + '\n')
					primer_output.write(leftprimers[i])
					primer_output.write('>' + 'primer' + str(i) + '-R' + '\n')
					primer_output.write(rightprimers[i])


		def poolPrimers():
			subprocess.call('./pooler')



		self.master = master
		self.input = ""

		self.output = ""
		self.param = ""
		self.inputbool = False
		self.outputbool = False
		self.parambool = False
		self.p3filestring = '-p3_settings_file='
		master.title("Complete Genomics Inc.")

		########## WIDGETS ##########
		entry_1 = Entry(master) #input
		entry_2 = Entry(master) #output
		entry_3 = Entry(master) #parameters

		label_1 = Label(master, text="AUTOPRIMER")
		button_1 = Button(master, text="Input Filepath: ", command=button1)
		button_2 = Button(master, text="Output Filepath: ", command=button2)
		button_3 = Button(master, text="Parameters Filepath: ", command=button3)
		button_get = Button(master, text="Get Primers", command=getPrimers)
		button_parse = Button(master, text="Parse Primers", command = PrimerParser)
		button_pool = Button(master, text="Pool Primers", command=poolPrimers)
		button_blast = Button(master, text="Blast Primers", command=doNothing)
		button_quit = Button(master, text="Quit", command=master.destroy)


		########## LAYOUT ##########
		label_1.grid(row=0, columnspan=4) #grid doesnt take left right, it takes NSEW directions
		button_1.grid(row=1, sticky=E, padx=1, pady=1)
		button_2.grid(row=2, sticky=E, padx=1, pady=1)
		button_3.grid(row=3, sticky=E, padx=1, pady=1)
		button_get.grid(row=4)
		button_parse.grid(row=4, sticky=W, column=1)
		button_pool.grid(row=4, sticky=W, column=2)
		button_blast.grid(row=4, sticky=W, column=3)
		button_quit.grid(row=4, sticky=W, column=4)

		entry_1.grid(row=1, column=1, sticky=W, padx=1, pady=1)
		entry_2.grid(row=2, column=1, sticky=W, padx=1, pady=1)
		entry_3.grid(row=3, column=1, sticky=W, padx=1, pady=1)






root = Tk()
autoprimer = AUTOPRIMER(root)
root.mainloop()
