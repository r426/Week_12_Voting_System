import tkinter as tk
import constants
from dataclass import DataClass


class VotingPage(tk.Frame):
    data = DataClass()
    parties = [data.party1, data.party2, data.party3, data.party4]

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.config(background="#ffeaa7")

        v = tk.IntVar()
        v.set(1)  # initializing the choice

        def todo():
            print(v.get())

        label = tk.Label(self, text="Please vote:", bg="#ffeaa7", font=constants.LARGE_FONT)
        label.pack(pady=18)

        for val, party in enumerate(self.parties):
            radio = tk.Radiobutton(self, text=party.name, bg="#ffeaa7", padx=20, font=constants.LARGE_FONT, variable=v,
                                   command=todo, value=val)
            radio.pack(anchor=tk.W, padx=217)

        button = tk.Button(self, text="Submit", bg="#55efc4", font=constants.LARGE_FONT,
                           command=lambda: exit())
        button.pack(pady=20)
