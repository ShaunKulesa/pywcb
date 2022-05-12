import os
from tkinter import Button, mainloop
import tkinter

from pyparsing import originalTextFor
from setuptools import Command

path = os.path.dirname(__file__).replace("\\", "/")

class Callback():
    def __init__(self):
        pass

    def get_parent(self):
        self.window = self.entry.nametowidget(self.entry.winfo_parent())
        loop = True
        
        while loop:
            parent = self.entry.nametowidget(self.window.winfo_parent())

            if parent.winfo_parent() == "":
                loop = False
        
            self.window = parent
    
    def create_callback(self, callback):
        self.window.tk.eval(f"source {path}/wcb3.7/wcb.tcl")
        self.window.tk.eval("package require wcb")
        self.window.tk.eval(callback)

class uppercase(Callback):
    command = "wcb::convStrToUpper"

    def __init__(self, entry):

        super().__init__()
        self.entry = entry
        self.get_parent()
        self.create_callback(f"wcb::callback {self.entry} before insert {self.command}")

class lower(Callback):
    command = "wcb::convStrToLower"

    def __init__(self, entry):
        super().__init__()
        self.entry = entry
        self.get_parent()
        self.create_callback(f"wcb::callback {self.entry} before insert {self.command}")

class alpha(Callback):
    command = "wcb::checkStrForAlpha"

    def __init__(self, entry):
        """
        Only allows alphabetic characters to be inputted into Entry and Text entrys
        """
       
        super().__init__()
        self.entry = entry
        self.get_parent()
        self.create_callback(f"wcb::callback {self.entry} before insert wcb::checkStrForAlpha")

class alnum(Callback):
    command = "wcb::checkStrForAlnum"

    def __init__(self, entry):
        """
        Only allows alphanumeric characters to be inputted into Entry and Text entrys
        """

        super().__init__()
        self.entry = entry
        self.get_parent()
        self.create_callback(f"wcb::callback {self.entry} before insert wcb::checkStrForAlnum")

class num(Callback):
    command = "wcb::checkStrForNum"

    def __init__(self, entry, case="Lower"):
        """
        Only allows numeric characters to be inputted into Entry and Text entrys
        """
    
        super().__init__()
        self.entry = entry
        self.get_parent()
        self.create_callback(f"wcb::callback {self.entry} before insert wcb::checkStrForNum")

class int(Callback):
    command = "wcb::checkEntryForInt"

    def __init__(self, entry):
        """
        Only allows intergers to be inputted into Entry entrys
        """

        super().__init__()
        self.entry = entry
        self.get_parent()
        self.create_callback(f"wcb::callback {self.entry} before insert wcb::checkEntryForInt")

class uint(Callback):
    command = "wcb::checkEntryUInt"

    def __init__(self, entry, max):
        """
        Only allows the max sized interger to be inputted into Entry entrys
        """

        super().__init__()
        self.entry = entry
        self.get_parent()
        max = "{" + "wcb::checkEntryForUInt " + str(max)  + "}"
        self.create_callback(f"wcb::callback {self.entry} before insert {max}")

class len(Callback):
    command = "wcb::checkEntryLen"

    def __init__(self, entry, len):
        """
        Only allows the max length to be inputted into Entry entrys
        """

        super().__init__()
        self.entry = entry
        self.get_parent()
        self.create_callback(f"wcb::callback {self.entry} before insert {{{self.command} {len}}}")

class real(Callback):
    command = "wcb::checkEntryReal"

    def __init__(self, entry):
        """
        Only allows real numbers to be inputted into Entry entrys
        """

        super().__init__()
        self.entry = entry
        self.get_parent()
        self.create_callback(f"wcb::callback {self.entry} before insert wcb::checkEntryForReal")

class fixed(Callback):
    command = "wcb::checkEntryForFixed"

    def __init__(self, entry, max):
        """
        Only allows fixed numbers to be inputted into Entry entrys
        """
            
        super().__init__()
        self.entry = entry
        self.get_parent()
        max = "{" + "wcb::checkEntryForFixed " + str(max)  + "}"
        self.create_callback(f"wcb::callback {self.entry} before insert {max}")

class combined(Callback):
    def __init__(self, entry, *args):            
        super().__init__()
        self.entry = entry

        args = list(args)

        for arg in args:
            args[args.index(arg)] = (arg.__dict__["command"])
        
        args = (' '.join(args))

        self.get_parent()

        self.create_callback(f"wcb::callback {self.entry} before insert {args}")