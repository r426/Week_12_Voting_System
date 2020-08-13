import tkinter as tk
from loginpage import LoginPage
from resultpage import ResultPage
import constants


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.config(background="#ffeaa7")

        label = tk.Label(self, text="Parliament Election 2020", bg="#ffeaa7", font=constants.LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="LOGIN", height=3, width=54, bg="#55efc4", font=constants.LARGE_FONT,
                            command=lambda: controller.show_frame(LoginPage))
        button1.pack()

        button2 = tk.Button(self, text="RESULT", height=3, width=54, bg="#00b894", font=constants.LARGE_FONT,
                            command=lambda: controller.show_frame(ResultPage))
        button2.pack()

        button3 = tk.Button(self, text="EXIT", height=3, width=54, bg="#55efc4", font=constants.LARGE_FONT,
                            command=lambda: exit())
        button3.pack()
