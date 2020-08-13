import tkinter as tk
import constants


class ErrorPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Error page!!!", font=constants.LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="Exit", command=lambda: exit())
        button.pack()
