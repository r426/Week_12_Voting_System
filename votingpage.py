import tkinter as tk
import constants
import globals


# global index


class VotingPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.config(background="#ffeaa7")

        index = tk.IntVar()
        index.set(0)  # initializing the choice

        def getindex():
            index.get()

        def incrementvotes(index):
            globals.parties[index].votes += 1
            print(globals.parties[index].votes)
            # from startpage import StartPage
            # controller.show_frame(StartPage)

        label = tk.Label(self, text="Please vote:", bg="#ffeaa7", font=constants.LARGE_FONT)
        label.pack(pady=18)

        for val, party in enumerate(globals.parties):
            radio = tk.Radiobutton(self, text=party.name, bg="#ffeaa7", padx=20, font=constants.LARGE_FONT,
                                   variable=index,
                                   command=lambda: getindex, value=val)
            radio.pack(anchor=tk.W, padx=217)

        button = tk.Button(self, text="Submit", bg="#55efc4", font=constants.LARGE_FONT,
                           command=lambda: incrementvotes(index.get()))
        button.pack(pady=20)
