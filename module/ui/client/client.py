from tkinter import *
from module.ui.client.iclient import IClient


class Client(IClient, Frame):
    def __init__(self, root, nickname, q, injector, **kwargs):
        Frame.__init__(self, root, **kwargs)
        self.nickname = nickname
        Button(self, text="Connect", command=self.connect_account).pack(fill=BOTH)
        self.client_socket = None
        self._q = q
        self._injector = injector

    def connect_account(self):
        self._injector.start_and_inject()
        self._q.put(self)
