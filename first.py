from tkinter import *
from main import *

def func1(psroot):
    menulist=Menu(psroot)
    psroot.config(menu=menulist)
    filemenu=Menu(menulist)
    menulist.add_command(label="file",menu=filemenu)