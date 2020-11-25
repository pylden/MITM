from module.protocol.network.message import Message


class IgnoredGetListMessage(Message):
    def __init__(self):
        self.id = 9731
