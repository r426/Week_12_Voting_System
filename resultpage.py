import tkinter as tk
import constants
import globals


class ResultPage(tk.Frame):

    def __init__(self, parent, controller):
        from startpage import StartPage
        tk.Frame.__init__(self, parent)
        self.config(background="#ffeaa7")
        for i in range(len(globals.parties)):
            exec(
                'tk.Label(self, text="%d. %s% d", bg="#ffeaa7", fg="#db0a63", font=constants.LARGE_FONT).pack(padx=175)' % (
                    i + 1, globals.parties[i].name, globals.parties[i].votes))

        button = tk.Button(self, text="Back", bg="#55efc4", font=constants.LARGE_FONT,
                           command=lambda: controller.show_frame(StartPage))
        button.pack(pady=25)
