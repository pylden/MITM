from module.protocol.network.message import Message


class IgnoredListMessage(Message):
    def __init__(self):
        self.id = 8697
