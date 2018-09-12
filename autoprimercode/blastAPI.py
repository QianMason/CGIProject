import Bio
from tkinter.filedialog import *
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

import requests
# blasturl = 'https://blast.ncbi.nlm.nih.gov/Blast.cgi?QUERY=ATCTTGGGGGCCATTTTTTACTGGCAA&DATABASE=nt&PROGRAM=blastn&CMD=Put'
#
# blasturljson = requests.get(blasturl)

root = Tk()
root.fileName = askopenfilename()

with open(root.fileName) as file:
    fstring = file.read()



fasta_string = fstring
print('line 11')
result_handle = NCBIWWW.qblast("blastn", "nt", fasta_string)
print('line 13')

with open("my_blast.xml", "w") as out_handle:
    out_handle.write(result_handle.read())
result_handle.close()

result_handle = open('my_blast.xml')

blast_record = NCBIXML.parse(result_handle) #changed from .read() for more than a single record
#for multiple sequences use .parse()
#blast_records = NCBIXML.parse(result_handle)

evalue = float(input('Please enter an e-value threshhold: '))

item = next(blast_record)

E_VALUE_THRESH = evalue

# need to add a file write to the thing so instead of printing it writes the information somewhere so that it can be displayed

while True:
    try:
        for alignment in item.alignments:
             for hsp in alignment.hsps:
                 if hsp.expect < E_VALUE_THRESH: #use this to determine if the result will be applicable / HAVE USER SET / default value?
                     print("****Alignment****")
                     print("sequence:", alignment.title)
                     print("length:", alignment.length)
                     print("e value:", hsp.expect)
                     print(hsp.query[0:75] + "...")
                     print(hsp.match[0:75] + "...")
                     print(hsp.sbjct[0:75] + "...")
        item = next(blast_record)
    except StopIteration:
        print("Done!")
        break
