from module.protocol.network.message import Message


class PaddockBuyResultMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9413
        self.paddockId = {"type": "Number", "value": ""}
        self.bought = {"type": "Boolean", "value": ""}
        self.realPrice = {"type": "Number", "value": ""}
