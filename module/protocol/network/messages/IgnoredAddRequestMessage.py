from module.protocol.network.message import Message


class IgnoredAddRequestMessage(Message):
    def __init__(self):
        self.id = 9784
        self.name = {"type": "String", "value": ""}
