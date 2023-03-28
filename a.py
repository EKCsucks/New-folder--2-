from tkinter import *
from tkinter import messagebox


def top():
    if not any(isinstance(x, Toplevel) for x in root.winfo_children()):
        toplevel = Toplevel(root)
        lbl = Label(toplevel, text='TopLevel')
        lbl.pack()

    else:

        messagebox.showinfo("showinfo", "Top level already exists")


root = Tk()

btn = Button(root, text='text', command=top)
btn.pack()

root.mainloop()