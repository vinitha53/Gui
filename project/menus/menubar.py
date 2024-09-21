from tkinter import *

from menus.editmenu import editmenulist
from menus.filemenu import filemenuitems
from menus.format_1 import formatlist
from menus.viewmenu import *

def menubar(psroot):
    menulist=Menu(psroot)
    psroot.config(menu=menulist)
    filemenuitems(menulist)
    editmenulist(menulist)
    formatlist(menulist)
    viewmenulist(menulist)
    





