from module.protocol.network.message import Message


class ExchangeBidPriceForSellerMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 3208
        self.allIdentical = {"type": "Boolean", "value": ""}
        self.minimalPrices = {"type": "Vector.<Number>", "value": ""}
