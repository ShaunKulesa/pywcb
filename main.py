from tkinter import *

import pywcb

window = Tk()

#Entry, Text,

# pywcb.upper()
entry = Entry(window)
entry.pack()
# pywcb.lower(entry)
# pywcb.alpha(entry)
# pywcb.alnum(entry)
# pywcb.num(entry)
# pywcb.int(entry)
# pywcb.uint(entry, max=100)
pywcb.len(entry, len=5)
# pywcb.real(entry)
# pywcb.fixed(entry, 2)
# pywcb.combined(entry, pywcb.upper, pywcb.alnum)

mainloop()
