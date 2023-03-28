from tkinter import *

root = Tk()
root.geometry('300x500')
root.title('Tkinter Hub')

head_frame = Frame(root, bg='#158aff', highlightbackground='white', highlightthickness=1)
def toggle_menu():
    def collapse_toggle_menu():
        toggle_menu_fm.destroy()
        #toggle_btn.config(activeforeground='white')
        toggle_btn(command=lambda: toggle_menu())

    toggle_menu_fm = Frame(root, bg='#158aff')

    window_height = 500
    toggle_menu_fm.place(x=0, y=50, height=window_height, width=200)
    #toggle_btn.config(activeforeground='black')
    toggle_btn.config(command=lambda: collapse_toggle_menu())




toggle_btn = Button(head_frame, text='☰', bg='#158aff', fg='white', font=('Bold', 20), bd=0, activebackground='#158aff',
                    activeforeground='white', command=lambda: toggle_menu())
toggle_btn.pack(side=LEFT)

head_frame.pack(side=TOP, fill=X)
head_frame.pack_propagate(False)
head_frame.configure(height=50)


root.mainloop()
