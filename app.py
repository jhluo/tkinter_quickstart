# -*- coding: utf-8 -*-
'''top level widgets'''

from tkinter import Frame
from Widgets.WidgetButton import WidgetButton

class App(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.msg_init()
        Frame.__init__( self, master )
        self.pack()
        self.create_widgets()

    def msg_init( self ):
        print("Init...")
    
    def create_widgets( self ):
        btnTest = WidgetButton.create( self )


