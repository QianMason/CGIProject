import subprocess
import tkinter as tk # import tkinter as tk is good for compatibility and maintainability. Don't use *
from tkinter.filedialog import *
import tkinter.messagebox
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

class AutoPrimer(tk.Tk): # Class names should normally use the CapWords convention.
    def __init__(self):
        #initialization
        tk.Tk.__init__(self)
        self.title("Complete Genomics Inc.")
        self.input = ""
        self.output = ""
        self.param = ""
        self.inputbool = False
        self.outputbool = False
        self.parambool = False
        self.p3filestring = '-p3_settings_file='


        self.entry_input = tk.Entry(self)
        self.entry_output = tk.Entry(self)
        self.entry_parameters = tk.Entry(self)
        self.entry_input.grid(row=1, column=1, padx=1, pady=1, sticky="w")
        self.entry_output.grid(row=2, column=1, padx=1, pady=1, sticky="w")
        self.entry_parameters.grid(row=3, column=1, padx=1, pady=1, sticky="w")

        self.label1 = tk.Label(self, text="AUTOPRIMER").grid(row=0, columnspan=4)
        tk.Button(self, text="Input Filepath: ", command=self.button1).grid(row=1, padx=1, pady=1, sticky="e")
        tk.Button(self, text="Output Filepath: ", command=self.button2).grid(row=2, padx=1, pady=1, sticky="e")
        tk.Button(self, text="Parameters Filepath: ", command=self.button3).grid(row=3, padx=1, pady=1, sticky="e")
        tk.Button(self, text="Get Primers", command=self.get_primers).grid(row=4)
        tk.Button(self, text="Parse Primers", command=self.primer_parser).grid(row=4, column=1, sticky="w")
        tk.Button(self, text="Pool Primers", command=self.pool_primers).grid(row=4, column=2, sticky="w")
        tk.Button(self, text="Blast Primers", command=lambda: BlastAPI(self)).grid(row=4, column=3, sticky="w")
        tk.Button(self, text="Quit", command=self.destroy).grid(row=4, column=4, sticky="w")

        #CLASS METHODS
        #Series of buttons methods that take in the filepath and displays it in the text widget to the user

    def button1(self):
        self.entry_input.delete(0,END)
        ifp = askopenfilename()
        self.setInput(ifp)
        self.entry_input.insert(0, ifp)
        self.setInputBool(True)
    def button2(self):
        self.entry_output.delete(0,END)
        ofp = asksaveasfilename()
        self.setOutput(ofp)
        self.entry_output.insert(0, ofp)
        self.setOutputBool(True)
    def button3(self):
        self.entry_parameters.delete(0,END)
        pfp = askopenfilename()
        self.entry_parameters.insert(0, pfp)
        self.setParameterBool(True)
    def buttonprint(self):
        tkinter.messagebox.showinfo('AUTOPRIMER', str(self.inputbool))

        #Methods that rely on class attributes after using above buttons to set
    def get_primers(self):
        print(self.inputbool, self.outputbool)
        if self.inputbool == False or self.outputbool == False:
            tkinter.messagebox.showinfo('AUTOPRIMER', 'No input file and/or output destination detected!')
        else:
            if self.parambool == False:
                outputlocation = '-output=' + self.output + 'primer3output.txt'
                cmd = ['primer3_core', outputlocation, self.input]
                subprocess.call(cmd)
            else: #parameters present
                outputlocation = '-output=' + self.output + 'primer3output.txt'
                p3filesettings = self.p3filestring + self.param
                cmd = ['primer3_core', p3filesettings, outputlocation, self.input]
                subprocess.call(cmd)

    def primer_parser(self):
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

    def pool_primers(self):
        subprocess.call('./pooler4')

        #Setters and Getters
    def setInput(self, value):
        self.input = value
    def setOutput(self, value):
        self.output = value
    def setParam(self, value):
        self.param = value
    def setInputBool(self, value):
        self.inputbool = value
    def setOutputBool(self, value):
        self.outputbool = value
    def setParameterBool(self, value):
        self.parambool = value




class BlastAPI(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.inputfile = ''
        self.title('Complete Genomics Inc.')
        self.e_value_thresh = ""

        self.e_value_setting = tk.Entry(self)
        self.e_value_setting.pack() # Used pack here for quick testing. You will need to work on geometry yourself.
        tk.Button(self, text="Close", command=self.destroy).pack()
        tk.Button(self, text="Input file", command=self.buttonfile).pack() #add method that does same thing for input button in autoprimer class
        tk.Button(self, text="Blast Primers", command=self.blast_primers).pack()

    def buttonfile(self):
        self.inputfile = askopenfilename()
        print(self.inputfile)

    def blast_primers(self): # Nothing is calling this function in your example.
        with open(self.inputfile) as file:
            string = file.read() # string is not being used here.

        fasta = string # No such var name in code.
        result_handle = NCBIWWW.qblast("blastn", "nt", fasta) # This had a typo NCBIWW instead of NCBIWWW.

        with open("my_blast.xml", "w") as out_handle:
            out_handle.write(result_handle.read())
        result_handle.close()

        result_handle = open('my_blast.xml')
        self.blast_record = NCBIXML.parse(result_handle)
        evalue = 1 # Is not being used here.
        self.item = next(self.blast_record)
        self.e_value_thresh = self.e_value_setting.get()
        self.blast_write_loop()


    def blast_write_loop(self):
        # I don't really like while loops and they have problems in event based GUI's.
        # I don't think a while loop is needed here anyway.
        with open('BlastResults.txt', 'w') as blast:
            try:
                for alignment in self.item.alignments:
                    for hsp in alignment.hsps:
                        if hsp.expect < self.e_value_thresh:
                            blast.write("****Alignment****")
                            blast.write("sequence:", alignment.title)
                            blast.write("length:", alignment.length)
                            blast.write("e value:", hsp.expect)
                            blast.write(hsp.query[0:75] + "...")
                            blast.write(hsp.match[0:75] + "...")
                            blast.write(hsp.sbjct[0:75] + "...")
                self.item = next(self.blast_record)
            except StopIteration:
                print("Done!")


autoprimer = AutoPrimer()
autoprimer.mainloop()
