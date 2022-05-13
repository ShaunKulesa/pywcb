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

class lowercase(Callback):
    command = "wcb::convStrToLower"

    def __init__(self, entry):
        super().__init__()
        self.entry = entry
        self.get_parent()
        self.create_callback(f"wcb::callback {self.entry} before insert {self.command}")

class alphabetic(Callback):
    command = "wcb::checkStrForAlpha"

    def __init__(self, entry):
       
        super().__init__()
        self.entry = entry
        self.get_parent()
        self.create_callback(f"wcb::callback {self.entry} before insert {self.command}")

class alphanumeric(Callback):
    command = "wcb::checkStrForAlnum"

    def __init__(self, entry):

        super().__init__()
        self.entry = entry
        self.get_parent()
        self.create_callback(f"wcb::callback {self.entry} before insert {self.command}")

class integer(Callback):
    command = "wcb::checkEntryForInt"

    def __init__(self, entry):

        super().__init__()
        self.entry = entry
        self.get_parent()
        self.create_callback(f"wcb::callback {self.entry} before insert {self.command}")

class maxinteger(Callback):
    command = "wcb::checkEntryUInt"

    def __init__(self, entry, maxint):

        super().__init__()
        self.entry = entry
        self.get_parent()
        self.create_callback(f"wcb::callback {self.entry} before insert {{{self.command} {maxint}}}")

class length(Callback):
    command = "wcb::checkEntryLen"

    def __init__(self, entry, maxlen):

        super().__init__()
        self.entry = entry
        self.get_parent()
        self.create_callback(f"wcb::callback {self.entry} before insert {{{self.command} {maxlen}}}")

class real(Callback):
    command = "wcb::checkEntryReal"

    def __init__(self, entry):
        super().__init__()
        self.entry = entry
        self.get_parent()
        self.create_callback(f"wcb::callback {self.entry} before insert {self.command}")

class fixed(Callback):
    command = "wcb::checkEntryForFixed"

    def __init__(self, entry, max):            
        super().__init__()
        self.entry = entry
        self.get_parent()
        self.create_callback(f"wcb::callback {self.entry} before insert {{{self.command} {max}}}")

class combined(Callback):
    def __init__(self, entry, *args):            
        super().__init__()
        self.entry = entry

        args = list(args)

        for arg in args:
            args[args.index(arg)] = arg.command
        
        args = (' '.join(args))

        self.get_parent()

        self.create_callback(f"wcb::callback {self.entry} before insert {args}")