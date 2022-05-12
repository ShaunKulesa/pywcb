def uppercase(entry):
    """
    Makes all input in the Entry widget uppercase.

    args:
        entry - The Entry widget to apply the validation to.
    """

def lowercase(entry):
    """
    Makes all input in the Entry widget lowercase.

    args:
        entry - The Entry widget to apply the validation to.    
    """

def alphabetic(entry):
    """
    Only allows alphabetic characters to be inputted into the Entry widget.

    args:
        entry - The Entry widget to apply the validation to.
    """

def alphanumeric(entry):
    """
    Only allows alphanumeric characters to be inputted into the Entry widget.

    args:
        entry - The Entry widget to apply the validation to.
    """

def numeric(entry):
    """
    Only allows numeric characters to be inputted into the Entry widget.

    args:
        entry - The Entry widget to apply the validation to.
    """

def integer(entry):
    """
    Only allows intergers to be inputted into the Entry widget.

    args:
        entry - The Entry widget to apply the validation to.
    """

def maxinteger(entry, maxint):
    """
    Only allows the max sized interger to be inputted into the Entry widget.

    args:
        entry - The Entry widget to apply the validation to.
            
        maxint - The max sized integer to allow.
    """

def length(entry, maxlen):
    """
    Only allows the the max length to be inputted into the Entry widget.

    args:
        entry - The Entry widget to apply the validation to.

        maxlen - The maximum length to be allowed
    """

def real(entry):
    """
    Only allows real numbers to be inputted into the Entry widget.

    args:
        entry - The Entry widget to apply the validation to.
    """

def fixed(entry, decimal_places):
    """
    This allows you to use fixed amount of decimal places to be inputted into the Entry widget.

    args:
        entry - The Entry widget to apply the validation to.

        decimal_places - The amount of decimal places to allow.
    """

def combined(entry, *conditions):
    """
    This allows you to use multiple conditions at once. 

    args:
        entry - The Entry widget to apply the validation to.

        conditions - The conditions to apply for the validation. For example pywcb.upper and pywcb.alnum
    
    examples:
    ```
        entry = tkinter.Entry()
        pywcb.combined(entry, pywcb.upper, pywcb.alnum)
        
        entry = tkinter.Entry()
        pywcb.combined(entry, pywcb.int, lambda:pywcb.len(3))
    ```
    """


