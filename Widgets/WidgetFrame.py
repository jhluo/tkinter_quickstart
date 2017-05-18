from tkinter import Frame as Frm

class WidgetFrame( Frm ):

  def create( self ):
    self.QUIT = Frm( self )
    self.QUIT["width"] = 800
    self.QUIT["height"] = 600
    self.QUIT.pack() 
    
  def __init__( self ):
    self.created = True 
