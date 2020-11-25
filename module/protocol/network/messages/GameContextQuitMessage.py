from module.protocol.network.message import Message


class GameContextQuitMessage(Message):
    def __init__(self):
        self.id = 8333
