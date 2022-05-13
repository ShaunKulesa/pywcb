from tkinter import *
import pywcb

window = Tk()

entry = Entry(window)
entry.pack()

pywcb.combined(entry, pywcb.uppercase, pywcb.alphanumeric)

pywcb.uppercase(entry)
pywcb.lowercase(entry)

pywcb.alphabetic(entry)
pywcb.alphanumeric(entry)
pywcb.integer(entry)
pywcb.maxinteger(entry, 100)
pywcb.fixed(entry, 2)
pywcb.real(entry)
pywcb.length(entry, 3)

mainloop()
