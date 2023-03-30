from tkinter import *
from settings import *
from login import *
from healthpage import *


class homepage:
    def __init__(self, root, previouscanvas):
        self.root = root
        previouscanvas.pack_forget()

        def toggle_menu():
            def collapse_toggle_menu():
                self.toggle_menu_fm.destroy()
                self.toggle_btn.config(command=toggle_menu)

            self.toggle_menu_fm = Frame(self.root, bg=primarycolor1)
            self.home_btn = Button(self.toggle_menu_fm, text="home", bg=primarycolor1, fg=secondarycolor1,
                                   font=header, bd=0,
                                   activebackground=primarycolor1)
            self.healthpge_btn = Button(self.toggle_menu_fm, text="personal health tracker", bg=primarycolor1,
                                        fg=secondarycolor1,
                                        font=header, bd=0,
                                        activebackground=primarycolor1, command=health_button)
            self.login_btn = Button(self.toggle_menu_fm, text="sign up/sign in", bg=primarycolor1, fg=secondarycolor1,
                                    font=header, bd=0,
                                    activebackground=primarycolor1, command=loginform)
            self.healthpge_btn.place(x=10, y=40)
            self.home_btn.place(x=10, y=20)
            self.login_btn.place(x=10, y=60)

            self.toggle_menu_fm.place(x=2, y=50, height=200, width=150, )
            self.toggle_btn.config(command=collapse_toggle_menu)

        self.bgcanvas = Canvas(root, width=1300, height=700, bg=backdrop)
        self.toggle_btn = Button(self.bgcanvas, text='≡', bg=primarycolor1, fg='white',
                                 font=iconfont, bd=0,
                                 activebackground=primarycolor1, command=toggle_menu)
        self.bgcanvas.create_rectangle((-1, 0), (1350, 50), fill=primarycolor1)
        self.bgcanvas.create_rectangle((100, 100), (1200, 400), fill=secondarycolor1, outline=secondarycolor1)
        self.bgcanvas.create_text((1150, 25), text="health association group", fill=backdrop, font=header)
        self.bgcanvas.place(x=0, y=0)

        self.toggle_btn.place(x=3, y=5)

        def health_button():
            from healthpage import healthtrackerpage
            healthtrackerpage(root, self.bgcanvas)
