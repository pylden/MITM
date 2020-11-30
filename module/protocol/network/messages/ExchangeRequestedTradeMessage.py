from module.protocol.network.messages.ExchangeRequestedMessage import ExchangeRequestedMessage


class ExchangeRequestedTradeMessage(ExchangeRequestedMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        ExchangeRequestedMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5850
        self.source = {"type": "Number", "value": ""}
        self.target = {"type": "Number", "value": ""}
