from module.protocol.network.message import Message


class ExchangeBidPriceForSellerMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 3208
        self.allIdentical = {"type": "Boolean", "value": ""}
        self.minimalPrices = {"type": "Vector.<Number>", "value": ""}
