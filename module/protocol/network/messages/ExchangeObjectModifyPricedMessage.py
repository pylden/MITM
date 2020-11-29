from module.protocol.network.messages.ExchangeObjectMovePricedMessage import ExchangeObjectMovePricedMessage


class ExchangeObjectModifyPricedMessage(ExchangeObjectMovePricedMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        ExchangeObjectMovePricedMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9325
