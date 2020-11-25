from module.protocol.network.message import Message


class ExchangeBidPriceMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 7344
        self.genericId = {"type": "uint", "value": ""}
        self.averagePrice = {"type": "Number", "value": ""}
