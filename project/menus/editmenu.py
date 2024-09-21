from tkinter import *


def editmenulist(ps_menulist):
    
    editmenu=Menu(ps_menulist,tearoff=0)

    ps_menulist.add_cascade(label="edit",menu=editmenu)
    editmenu.add_command(label="Undo",underline=0,accelerator="Ctrl+Z")
    # editmenu.
    editmenu.add_command(label="cut",underline=0,accelerator="Ctrl+X")
    editmenu.add_command(label="Copy",underline=2,accelerator="Ctrl+c")
    editmenu.add_command(label="Paste",underline=0,accelerator="Ctrl+V")
    editmenu.add_separator()
    editmenu.add_command(label="Delete",accelerator="del")
    editmenu.add_command(label="Replace",underline=0,accelerator="Ctrl+H")
    editmenu.add_command(label="Goto",underline=0,accelerator="Ctrl+G")
    editmenu.add_separator()
    editmenu.add_command(label="SelectAll",underline=0,accelerator="Ctrl+A")
    editmenu.add_command(label="Time/Date",underline=0,accelerator="f5")
    
