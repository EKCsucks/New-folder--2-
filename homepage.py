from tkinter import *
from colorsandfonts import *

class homepage:
    def __init__(self,root):
        self.root = root
        
        self.bgcanvas = Canvas(root, width=1300, height=700, bg=backdrop)
        self.bgcanvas.create_rectangle((-1, -20), (1350, 50), fill='#1282A2')
        
        self.bgcanvas.create_text((1150, 25),text="health association group",fill=backdrop,font=header)
        self.bgcanvas.place(x = -1 ,y =-1)

        
        