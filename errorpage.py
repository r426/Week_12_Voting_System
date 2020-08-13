import tkinter as tk
import constants


class ErrorPage(tk.Frame):

    def __init__(self, parent, controller):
        from startpage import StartPage
        tk.Frame.__init__(self, parent)
        self.config(background="#ffeaa7")
        label = tk.Label(self, text="Wrong name and/or ID.", bg="#ffeaa7", fg="#db0a63", font=constants.LARGE_FONT)
        label.pack(pady=71, padx=175)

        button = tk.Button(self, text="Back", bg="#55efc4", font=constants.LARGE_FONT,
                           command=lambda: controller.show_frame(StartPage))
        button.pack(pady=25)
