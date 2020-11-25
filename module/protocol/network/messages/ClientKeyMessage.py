from module.protocol.network.message import Message


class ClientKeyMessage(Message):
    def __init__(self):
        self.id = 6268
        self.key = {"type": "String", "value": ""}
