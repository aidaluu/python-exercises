from tkinter import *

def addUp():
    i = TKinteger.get() # read
    i += 1
    TKinteger.set(i) # write

window = Tk() # create main window

TKinteger = IntVar()
#TKstring = StringVar()

teksti = Label(window, textvariable=TKinteger)
teksti.grid(column=0,row=0,columnspan=2)

input = Entry(window)
input.grid(column=0, row=1)

button = Button(window, text="Hardest button to button", command=addUp)
button.grid(column=1, row=1)

window.mainloop()
