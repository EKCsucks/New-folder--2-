from tkinter import *
from colorsandfonts import *

class loginform:
    def __init__(self):
        self.root2 = Toplevel()
        self.root2.geometry("200x100")



        # Create exit button.
        self.button = Button(self.root2, text="Exit", command=self.root2.destroy)

        self.label.pack()
        self.button.pack()

        # Display until closed manually.
        self.root2.mainloop()
