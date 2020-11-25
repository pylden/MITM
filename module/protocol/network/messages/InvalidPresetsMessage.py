from module.protocol.network.message import Message


class InvalidPresetsMessage(Message):
    def __init__(self):
        self.id = 2448
