from tkinter import Button as Btn
from tkinter import Frame as Frm
from tkinter import messagebox

class WidgetButton(Btn):
  
  def create( self ):
    self.QUIT = Btn( self )
    self.QUIT["text"] = "Sair"
    self.QUIT["fg"] = "#fff"
    self.QUIT["bg"] = "#333"
    self.QUIT["width"] = 100
    self.QUIT["height"] = 20
    self.QUIT["command"] = self.quit
    self.QUIT.pack({"side": "left"})

  def __init__( self ):
    self.create()
