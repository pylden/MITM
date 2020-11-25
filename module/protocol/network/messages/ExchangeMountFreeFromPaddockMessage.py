from module.protocol.network.message import Message


class ExchangeMountFreeFromPaddockMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9283
        self.name = {"type": "String", "value": ""}
        self.worldX = {"type": "int", "value": ""}
        self.worldY = {"type": "int", "value": ""}
        self.liberator = {"type": "String", "value": ""}
