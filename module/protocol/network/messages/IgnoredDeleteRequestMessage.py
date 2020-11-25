from module.protocol.network.message import Message


class IgnoredDeleteRequestMessage(Message):
    def __init__(self):
        self.id = 7856
