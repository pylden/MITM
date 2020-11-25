from module.protocol.network.message import Message


class PaddockSellRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 647
        self.price = {"type": "Number", "value": ""}
        self.forSale = {"type": "Boolean", "value": ""}
