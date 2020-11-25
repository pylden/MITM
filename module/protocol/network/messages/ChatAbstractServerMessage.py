from module.protocol.network.message import Message


class ChatAbstractServerMessage(Message):
    def __init__(self):
        self.id = 1532
        self.content = {"type": "String", "value": ""}
        self.fingerprint = {"type": "String", "value": ""}
