from module.protocol.network.messages.ExchangeObjectMoveMessage import ExchangeObjectMoveMessage


class ExchangeObjectMovePricedMessage(ExchangeObjectMoveMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        ExchangeObjectMoveMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 763
        self.price = {"type": "Number", "value": ""}
