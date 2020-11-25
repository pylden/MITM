from module.protocol.network.message import Message


class ExchangeMountFreeFromPaddockMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9283
        self.name = {"type": "String", "value": ""}
        self.liberator = {"type": "String", "value": ""}
