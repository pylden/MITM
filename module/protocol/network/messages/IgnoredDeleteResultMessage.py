from module.protocol.network.message import Message


class IgnoredDeleteResultMessage(Message):
    def __init__(self):
        self.id = 5614
        self.name = {"type": "String", "value": ""}
