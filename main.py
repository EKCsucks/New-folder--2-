from tkinter import *
from homepage import *  # imports the class from the other file


class basicform:
    def __init__(self):
        self.root = Tk()
        # creates a window of a fixed size
        self.root.geometry("1300x700")
        self.root.resizable(False, False)
        self.root.title('')
        # calls on the class form another file
        home = homepage(self.root)
        self.root.mainloop()


if __name__ == "__main__":
    # checks the code is being run form main then runs the class in this function
    window = basicform()

