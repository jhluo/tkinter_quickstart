# -*- coding: utf-8 -*-
'''main module that boostraps the application'''

from tkinter import Tk
from app import App

# top level widget
root = Tk() # pylint: disable=invalid-name
root.geometry("600x400+300+300")

main = App(master=root) # pylint: disable=invalid-name
main.master.title("Application Title")
root.protocol("WM_DELETE_WINDOW", App.on_closing)
main.mainloop()
root.destroy()
