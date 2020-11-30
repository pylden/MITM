from module.protocol.network.messages.ExchangeBidPriceMessage import ExchangeBidPriceMessage


class ExchangeBidPriceForSellerMessage(ExchangeBidPriceMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        ExchangeBidPriceMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3208
        self.allIdentical = {"type": "Boolean", "value": ""}
        self.minimalPrices = {"type": "Vector.<Number>", "value": ""}
