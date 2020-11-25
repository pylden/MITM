from module.protocol.network.message import Message


class EmotePlayErrorMessage(Message):
    def __init__(self):
        self.id = 7072
