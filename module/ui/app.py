from tkinter import *
from module.ui.client.client import Client


class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self._root_init()
        self._init_ui()

    def _root_init(self):
        self.geometry("800x600")
        self.title("Dofus Packet Analyzer")
        # for r in range(6):
        #     self.rowconfigure(r, weight=1)
        #     self.columnconfigure(r, weight=1)

    def _init_ui(self):
        pass
        #  Account Frame
        # self._account_frame = Frame(self)
        # self._add_account_button = Button(self._account_frame, text="+ Add Account",
        #                                   command=self.show_add_account)
        # self._account_frame.grid(row=0, column=0, rowspan=6, columnspan=1, sticky=W+E+N+S)
        # self._add_account_button.pack(fill=BOTH)

        #  Content Frame
        # self._content_frame = Frame(self)
        # self._content_frame.grid(row=0, column=1, rowspan=6, columnspan=5, sticky=W+E+N+S)

    # def show_add_account(self):
    #     username = StringVar()
    #     password = StringVar()
    #     nickname = StringVar()
    #     popup = Toplevel(self)
    #     popup.title("Add Account")
    #     popup.geometry("300x160")
    #     for num in range(3):
    #         popup.rowconfigure(num, weight=1)
    #
    #     Label(popup, text="Username : ").grid(row=0, column=0, rowspan=1, padx=5, pady=5)
    #     Entry(popup, textvariable=username).grid(row=0, column=1, columnspan=2)
    #     Label(popup, text="Password : ").grid(row=1, column=0, rowspan=1)
    #     Entry(popup, textvariable=password).grid(row=1, column=1, columnspan=2)
    #     Label(popup, text="Nickname : ").grid(row=2, column=0, rowspan=1)
    #     Entry(popup, textvariable=nickname).grid(row=2, column=1, columnspan=2)
    #     Button(popup, text="Validate",
    #            command=lambda: self.add_account(username.get(), password.get(), nickname.get(), popup))\
    #         .grid(column=1, rowspan=1)

    # def add_account(self, username, password, nickname, popup):
    #     Button(self._account_frame, text=nickname, command=lambda: self.show_account(nickname)).pack(fill=BOTH)

    # def update_current_frame(self, frame):
    #     if self._current_account_frame is not None:
    #         self._current_account_frame.grid_remove()
    #     self._current_account_frame = frame
    #     self._current_account_frame.grid(row=0, column=1, rowspan=6, columnspan=5, sticky=W+E+N+S)
    #
    # def show_account(self, nickname):
    #     self.update_current_frame(self._accounts[nickname]['frame'])
