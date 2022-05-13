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
    Only allows alphabetic characters to be inserted into the Entry widget.

    args:

        entry - The Entry widget to apply the validation to.
    """

def alphanumeric(entry):
    """
    Only allows alphanumeric characters to be inserted into the Entry widget.

    args:

        entry - The Entry widget to apply the validation to.
    """

def numeric(entry):
    """
    Only allows numeric characters to be inserted into the Entry widget.

    args:

        entry - The Entry widget to apply the validation to.
    """

def integer(entry):
    """
    Only allows intergers to be inserted into the Entry widget.

    args:
        entry - The Entry widget to apply the validation to.
    """

def maxinteger(entry, maxint):
    """
    Only allows a certainly sized interger to be inserted into the Entry widget.

    args:

        entry - The Entry widget to apply the validation to.
            
        maxint - The maximum sized integer to be allowed.
    """

def length(entry, maxlen):
    """
    Only allows a certain length to be inserted into the Entry widget.

    args:

        entry - The Entry widget to apply the validation to.

        maxlen - The maximum length to be allowed
    """

def real(entry):
    """
    Only allows real numbers to be inserted into the Entry widget.

    args:

        entry - The Entry widget to apply the validation to.
    """

def fixed(entry, decimal_places):
    """
    Only allows float numbers with a certain number of decimal places to be inserted into the Entry widget.

    args:

        entry - The Entry widget to apply the validation to.

        decimal_places - The amount of decimal places to be allowed.
    """

def combined(entry, *conditions):
    """
    This function allows for multiple conditions to be combined and used together.

    args:

        entry - The Entry widget to apply the validation to.
        
        conditions - The conditions to be applied for the validation. For example pywcb.upper and pywcb.alnum
    
    examples:
    ```
        entry = tkinter.Entry()
        pywcb.combined(entry, pywcb.upper, pywcb.alnum)
        
        entry = tkinter.Entry()
        pywcb.combined(entry, pywcb.int, lambda:pywcb.len(3))
    ```
    """