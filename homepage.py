from tkinter import *
from colorsandfonts import *
from login import *

class homepage:
    def __init__(self, root):
        self.root = root
        
        self.bgcanvas = Canvas(root, width=1300, height=700, bg=backdrop)
        self.bgcanvas.create_rectangle((-1, 0), (1350, 50), fill=primarycolor1)
        self.bgcanvas.create_rectangle((100, 100), (1200, 400), fill=secondarycolor1)
        self.bgcanvas.create_text((1150, 25), text="health association group", fill=backdrop, font=header)
        self.bgcanvas.place(x=0, y=0)
        self.button = Button(self.bgcanvas, text ="open toplevel1", command = loginform)
        self.button.place(x=155, y=50)

        
        