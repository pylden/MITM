from module.protocol.network.message import Message


class ProtocolRequired(Message):
    def __init__(self):
        self.id = 5481
        self.version = {"type": "String", "value": ""}
