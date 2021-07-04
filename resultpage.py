import tkinter as tk
import constants
import globals


class ResultPage(tk.Frame):

    def __init__(self, parent, controller):
        from startpage import StartPage
        tk.Frame.__init__(self, parent)
        self.update()
        button1 = tk.Button(self, text="Update", bg="#55efc4", font=constants.LARGE_FONT,
                            command=lambda: self.update())
        button2 = tk.Button(self, text="Back", bg="#55efc4", font=constants.LARGE_FONT,
                            command=lambda: controller.show_frame(StartPage))
        button1.pack(pady=22)
        button2.pack(pady=22)

    def update(self):
        self.config(background="#ffeaa7")
        for i in range(len(globals.parties)):
            # FIXME override updates instead of adding them up at the bottom. pack –> place?
            lbl = 'tk.Label(self, text="%d. %s% d", bg="#ffeaa7", fg="#db0a63", font=constants.LARGE_FONT).pack(padx=230)' % (
                i + 1, globals.parties[i].name, globals.parties[i].votes)
            exec(lbl)
