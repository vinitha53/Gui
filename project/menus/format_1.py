from tkinter import *

def formatlist(ps_menulist):
    formatmenu=Menu(ps_menulist,tearoff=0)
    ps_menulist.add_cascade(label="Format",menu=formatmenu)

    formatmenu.add_command(label="Word wrap")
    formatmenu.add_command(label="font")