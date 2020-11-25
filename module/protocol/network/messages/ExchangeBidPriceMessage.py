from module.protocol.network.message import Message


class ExchangeBidPriceMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 7344
        self.genericId = {"type": "uint", "value": ""}
        self.averagePrice = {"type": "Number", "value": ""}
