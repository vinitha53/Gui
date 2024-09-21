from tkinter import *
def viewmenulist(ps_menulist):
    viewmenu=Menu(ps_menulist, tearoff=0)
    ps_menulist.add_cascade(label="view",menu=viewmenu)
    submenu=Menu(viewmenu,tearoff=0)
    
    viewmenu.add_cascade(label="zoom",menu=submenu)
    submenu.add_command(label="zoom in",accelerator="Ctrl++")
    submenu.add_command(label="zoom out",accelerator="Ctrl+-")
    submenu.add_command(label="restore the default zoom",accelerator="Ctrl+0")


    viewmenu.add_command(label="status bar")

    
    