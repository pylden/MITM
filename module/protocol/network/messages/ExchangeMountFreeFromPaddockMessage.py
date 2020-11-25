from module.protocol.network.message import Message


class ExchangeMountFreeFromPaddockMessage(Message):
    def __init__(self):
        self.id = 9283
        self.name = {"type": "String", "value": ""}
        self.liberator = {"type": "String", "value": ""}
