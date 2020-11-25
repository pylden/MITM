from module.protocol.network.message import Message


class ExchangeBidHouseBuyResultMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 3583
        self.uid = {"type": "uint", "value": ""}
        self.bought = {"type": "Boolean", "value": ""}
