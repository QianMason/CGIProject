from tkinter import *

root = Tk() #interface object thing
#theLabel = Label(root, text="This is too easy") #this is a label that you can put text in, first arg is where it goes
#theLabel.pack() #essentially fits whatever .pack() is being called on into wherever it can

topFrame = Frame(root) #invisible container going in the main window (root)
topFrame.pack() #anytime you want to display it has to be packed (anywhere)
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text='Button 1', fg='red') #parameters accepted: what frame, text on button, color of button (optional)
button2 = Button(topFrame, text='Button 2', fg='blue')
button3 = Button(topFrame, text='Button 3', fg='green')
button4 = Button(bottomFrame, text='Button 4', fg='purple')

button1.pack(side=TOP)
button2.pack(side=LEFT)
button3.pack(side=RIGHT)
button4.pack(side=BOTTOM)

root.mainloop() #keeps the window open indefinitely until the user terminates it
