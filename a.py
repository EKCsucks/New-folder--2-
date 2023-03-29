from tkinter import *

root = Tk()
root.geometry('300x500')
root.title('Tkinter Hub')


def toggle_menu():
    def collapse_toggle_menu():
        toggle_menu_fm.destroy()
        toggle_btn.config(command=toggle_menu)

    toggle_menu_fm = Frame(root, bg='lightblue')
    home_btn = Button(toggle_menu_fm, text="home", bg='lightblue', fg='white', font=('Bold', 20), bd=0)
    home_btn.place(x=20,y=20)
    window_height = root.winfo_height()
    toggle_menu_fm.place(x=0, y=50, height=window_height, width=200, )
    toggle_btn.config(command=collapse_toggle_menu)


head_frame = Frame(root, bg='lightblue', highlightbackground='white', highlightthickness=1)

toggle_btn = Button(head_frame, text='≡', bg='lightblue', fg='white', font=('Bold', 20), bd=0,
                    activebackground="lightblue", command=toggle_menu)

toggle_btn.pack(side=LEFT)

title_lb = Label(head_frame, text='Tkinter hub', bg='lightblue', fg='white', font=('Bold', 20))

title_lb.pack(side=LEFT)

head_frame.pack(side=TOP, fill=X)
head_frame.pack_propagate(False)
head_frame.configure(height=50)

root.mainloop()
