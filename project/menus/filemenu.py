from tkinter import *


def filemenuitems(pass_menulist):
    filemenu=Menu(pass_menulist, tearoff=0)
    pass_menulist.add_cascade(label="File", menu=filemenu)
    
    filemenu.add_command(label="new", underline=0, accelerator="Ctrl+N")
    filemenu.add_command(label="new window", underline=5, accelerator="Ctrl+Shift+N")
    filemenu.add_command(label="Open", underline=0, accelerator="Ctrl+O")
    filemenu.add_command(label="save", underline=0, accelerator="Ctrl+S")
    filemenu.add_command(label="Save As", underline=0, accelerator="Ctrl+Shift+S")
    filemenu.add_separator()
    filemenu.add_command(label="Page setup")
    filemenu.add_command(label="print", underline=0, accelerator="Ctrl+P")
    filemenu.add_separator()
    filemenu.add_command(label="exit", underline=0, accelerator="Ctrl+E")
    # emenu1(menulist)