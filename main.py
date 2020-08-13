# The code for navigation between windows was derived from:
# http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# License: http://creativecommons.org/licenses/by-sa/3.0/

# https://pythonprogramming.net/change-show-new-frame-tkinter/

import tkinter as tk
from functools import partial

LARGE_FONT = ("Verdana", 12)


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Parliament Election 2020")

        container = tk.Frame(self)
        container.config(background="#ffeaa7")
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="n")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.config(background="#ffeaa7")

        label = tk.Label(self, text="Parliament Election 2020", bg="#ffeaa7", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="LOGIN", height=3, width=54, bg="#55efc4", font=LARGE_FONT,
                            command=lambda: controller.show_frame(PageOne))
        button1.pack()

        button2 = tk.Button(self, text="RESULT", height=3, width=54, bg="#00b894", font=LARGE_FONT,
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()

        button3 = tk.Button(self, text="EXIT", height=3, width=54, bg="#55efc4", font=LARGE_FONT,
                            command=lambda: exit())
        button3.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.config(background="#55efc4")

        # username label and text entry box
        usernameLabel = tk.Label(self, text="Full Name", bg="#55efc4", font=LARGE_FONT)
        username = tk.StringVar()
        usernameEntry = tk.Entry(self, textvariable=username)
        usernameLabel.pack(pady=20, padx=231)
        usernameEntry.pack()

        # password label and password entry box
        passwordLabel = tk.Label(self, text="Voter ID", bg="#55efc4", font=LARGE_FONT)
        password = tk.StringVar()
        passwordEntry = tk.Entry(self, textvariable=password, show='*')
        passwordLabel.pack(pady=20)
        passwordEntry.pack()

        validateLogin = partial(self.validateLogin, username, password)

        # login button
        loginButton = tk.Button(self, text="Login", bg="#ffeaa7", font=LARGE_FONT, command=validateLogin)
        loginButton.pack(pady=25)

    def validateLogin(self, username, password):
        print("username entered :", username.get())
        print("password entered :", password.get())
        return


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # password label and password entry box
        passwordLabel = tk.Label(self, text="Password")
        password = tk.StringVar()
        passwordEntry = tk.Entry(self, textvariable=password, show='*')
        passwordLabel.pack(pady=5, padx=5)
        passwordEntry.pack(pady=5, padx=5)

        button2 = tk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


app = SeaofBTCapp("nnn")
app.mainloop()
