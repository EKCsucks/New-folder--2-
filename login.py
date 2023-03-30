from tkinter import *
from settings import *
from database import *


class loginform:
    def __init__(self):
        self.roottp = Toplevel()
        self.roottp.geometry("400x600")
        self.roottp.resizable(False, False)
        self.password = StringVar()
        self.user = StringVar(value='')

        def find_user():
            email = self.user.get()
            database = r"userdata.db"
            conn = create_connection(database)
            check_email_exists(conn, email)

        self.bgcanvas = Canvas(self.roottp, width=400, height=600, bg=backdrop)
        self.bgcanvas.create_rectangle((25, 25), (375, 575), fill=secondarycolor1)
        self.button = Button(self.bgcanvas, text="open toplevel1", command=loginform)
        self.username_txt = Entry(self.bgcanvas, width=25, textvariable=self.user, bg=backdrop, font=loginfont)
        self.password_txt = Entry(self.bgcanvas, height=1, textvariable=self.password, width=25, bg=backdrop, font=loginfont)
        self.toggle_btn = Button(self.bgcanvas, text='≡', bg=primarycolor1, fg='white',
                                 font=iconfont, bd=0,
                                 activebackground=primarycolor1, command=find_user)

        self.bgcanvas.place(x=0, y=0)
        self.username_txt.place(x=95, y=350)
        self.password_txt.place(x=95, y=400)
        self.toggle_btn.place(x=1, y=1)
        self.roottp.mainloop()


