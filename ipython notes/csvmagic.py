import pandas as pd
from io import StringIO

def csv(line,cell):
    sio - StringIO(cell)
    return pd.read_csv(sio)

def load_ipython_extension(ipython):
    """ 
    This function is called when the extension is loaded.
    It accepts an IPython InteractiveShell instance.
    we can register_magic with the 'register_magic_function' method.
    """
    ipython.register_magic_function(csv, 'cell')