# The code for navigation between windows was derived from:
# http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# License: http://creativecommons.org/licenses/by-sa/3.0/

# https://pythonprogramming.net/change-show-new-frame-tkinter/

import tkinter as tk
from startpage import StartPage
from loginpage import LoginPage
from resultpage import ResultPage
from votingpage import VotingPage
from errorpage import ErrorPage


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

        for F in (StartPage, LoginPage, ResultPage, VotingPage, ErrorPage):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="n")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


app = SeaofBTCapp()
app.mainloop()
