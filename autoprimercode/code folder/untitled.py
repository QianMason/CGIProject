from tkinter import *
import subprocess as sub
p = sub.Popen('./pooler',stdout=sub.PIPE,stderr=sub.PIPE)
print('line 4')
output, errors = p.communicate()
print('line 5')
root = Tk()
text = Text(root)
text.pack()
text.insert(END, output)
root.mainloop()
