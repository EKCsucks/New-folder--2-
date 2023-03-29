from tkinter import *
from settings import *


class loginform:
    def __init__(self):
        self.roottp = Toplevel()
        self.roottp.geometry("400x600")
        self.roottp.resizable(False, False)

        self.bgcanvas = Canvas(self.roottp, width=400, height=600, bg=backdrop)
        self.bgcanvas.create_rectangle((25, 25), (375, 575), fill=secondarycolor1)
        self.button = Button(self.bgcanvas, text="open toplevel1", command=loginform)
        self.inputtxt = Text(self.bgcanvas, height=1, width=25, bg=backdrop)

        self.bgcanvas.place(x=0, y=0)
        self.inputtxt.place(x=95, y=350)
        # Display until closed manually.
        self.roottp.mainloop()
