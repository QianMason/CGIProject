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
        #class attributes
        self.inputfile = ''
        self.inputboolean = False
        self.title('Complete Genomics Inc.')
        self.database = 'nt'
        self.searchtype = 'blastn'
        self.e_value_thresh = ""
        mainframe = tk.Frame(self)
        self.e_value_setting = tk.Entry(mainframe)
        mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
        mainframe.columnconfigure(0, weight = 1)
        mainframe.rowconfigure(0, weight = 1)
        mainframe.pack(pady = 50, padx = 100)
        self.tkvar1 = tk.StringVar(self)
        self.tkvar2 = tk.StringVar(self)
        # List with options
        searchchoices = ['blastn', 'megablast', 'blastp', 'blastx', 'tblastn', 'tblastx']
        databasechoices = ['nt','refseq_rna','refseq_representative_genomes','refseq_genomes','wgs', 'est', 'SRA', 'TSA', 'HTGS', 'pat', 'refseq_genomic']
        self.tkvar1.set(databasechoices[0]) # set the default option
        self.tkvar2.set(searchchoices[0])

        popupMenu = OptionMenu(mainframe, self.tkvar1, *databasechoices)
        popupMenu2 = OptionMenu(mainframe, self.tkvar2, *searchchoices)
        tk.Label(mainframe, text="Please select a file to input").grid(row = 1, column = 1)
        tk.Label(mainframe, text="Please select a database").grid(row = 3, column = 1)
        tk.Label(mainframe, text="Please select search type").grid(row = 5, column = 1)
        tk.Label(mainframe, text="Please specify an e-level cutoff").grid(row = 7, column = 1)
        popupMenu.grid(row = 4, column = 1)
        popupMenu2.grid(row = 6, column = 1)
        self.e_value_setting.grid(row = 8, column = 1) # Used pack here for quick testing. You will need to work on geometry yourself.
        #tk.Button(mainframe, text="Close", command=self.destroy).grid(row = 7, column = 1)
        tk.Button(mainframe, text="Input file", command=self.buttonfile).grid(row = 2, column = 1) #add method that does same thing for input button in autoprimer class
        tk.Button(mainframe, text="Blast Primers", command=self.blast_primers).grid(row = 9, column = 1, pady = 20)
        self.tkvar1.trace('w', self.change_database)
        self.tkvar2.trace('w', self.change_searchtype)

    #class methods that link to dropdown
    def change_database(self, *args):
        self.database = self.tkvar1.get()

    def change_searchtype(self, *args):
        self.searchtype = self.tkvar2.get()




    def buttonfile(self):
        self.inputfile = askopenfilename()
        self.inputboolean = True

    def blast_primers(self): # Nothing is calling this function in your example.
        if (self.inputboolean == True):
            # with open(self.inputfile) as file:
            #     string = file.read() # string is not being used here.
            #
            # fasta = string # No such var name in code.
            # print("line149")
            # result_handle = NCBIWWW.qblast(self.searchtype, self.database, fasta) # This had a typo NCBIWW instead of NCBIWWW.
            # print('line151')
            # with open("my_blast.xml", "w") as out_handle:
            #     out_handle.write(result_handle.read())
            # result_handle.close()
            # print('line155')
            result_handle = open('my_blast.xml')
            self.blast_record = NCBIXML.parse(result_handle)
            self.item = next(self.blast_record)
            #self.e_value_thresh = float(self.e_value_setting.get())
            self.e_value_thresh = 10
            self.blast_write_loop()
        else:
            tkinter.messagebox.showinfo('AUTOPRIMER', 'No input file detected! Please load an input file in FASTA format.')

    # def blast_write_loop(self):
    #     # I don't really like while loops and they have problems in event based GUI's.
    #     # I don't think a while loop is needed here anyway.
    def blast_write_loop(self):
        count = 0
        while True:
            with open('BlastResults.txt', 'a') as blast:
                try:
                    tkinter.messagebox.showinfo('AUTOPRIMER', str(count))
                    for alignment in self.item.alignments:
                        #print(alignment)
                        for hsp in alignment.hsps:
                            if hsp.expect < self.e_value_thresh:
                                blast.write("****Alignment****")
                                print("****Alignment****")
                                blast.write("sequence: " + str(alignment.title) + '\n')
                                print("sequence:", alignment.title)
                                blast.write("length: " + str(alignment.length) + '\n')
                                print("length:", alignment.length)
                                blast.write("e value: " + str(hsp.expect) + '\n')
                                print("e value:", hsp.expect)
                                blast.write(hsp.query[0:75] + "..."  + '\n')
                                print(hsp.query[0:75] + "...")
                                blast.write(hsp.match[0:75] + "..." + '\n')
                                print(hsp.match[0:75] + "...")
                                blast.write(hsp.sbjct[0:75] + "..." + '\n')
                                print(hsp.match[0:75] + "...")

                    self.item = next(self.blast_record)
                    count += 1

                except StopIteration:
                    blast.close()
                    tkinter.messagebox.showinfo('AUTOPRIMER', 'Sequences finished blasting!')
                    break



autoprimer = AutoPrimer()
autoprimer.mainloop()
