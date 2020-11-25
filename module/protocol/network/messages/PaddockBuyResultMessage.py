from module.protocol.network.message import Message


class PaddockBuyResultMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9413
        self.paddockId = {"type": "Number", "value": ""}
        self.bought = {"type": "Boolean", "value": ""}
        self.realPrice = {"type": "Number", "value": ""}
