import tkinter as tk
from functools import partial
from votingpage import VotingPage
from errorpage import ErrorPage
from person import Person
import globals
import constants


class LoginPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.config(background="#55efc4")

        # username label and text entry box
        usernameLabel = tk.Label(self, text="Full Name", bg="#55efc4", font=constants.LARGE_FONT)
        username = tk.StringVar()
        usernameEntry = tk.Entry(self, textvariable=username)
        usernameLabel.pack(pady=20, padx=231)
        usernameEntry.pack()

        # id label and id entry box
        idLabel = tk.Label(self, text="Voter ID", bg="#55efc4", font=constants.LARGE_FONT)
        userid = tk.StringVar()
        idEntry = tk.Entry(self, textvariable=userid, show='*')
        idLabel.pack(pady=20)
        idEntry.pack()

        validateLogin = partial(self.validateLogin, username, userid, usernameEntry, idEntry, controller)

        # login button
        loginButton = tk.Button(self, text="Login", bg="#ffeaa7", font=constants.LARGE_FONT, command=validateLogin)
        loginButton.pack(pady=25)

    def validateLogin(self, username, userid, usernameEntry, idEntry, controller):

        validuser = False
        input = Person(username.get(), userid.get())
        for user in globals.users:
            if user.username == input.username and user.userid == input.userid:
                validuser = True
        usernameEntry.delete(0, 'end')
        idEntry.delete(0, 'end')
        if (validuser):
            controller.show_frame(VotingPage)
        else:
            controller.show_frame(ErrorPage)
        return
