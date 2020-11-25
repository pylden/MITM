from module.protocol.network.message import Message


class BasicTimeMessage(Message):
    def __init__(self):
        self.id = 1002
