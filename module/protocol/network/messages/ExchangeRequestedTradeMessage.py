from module.protocol.network.message import Message


class ExchangeRequestedTradeMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 5850
        self.source = {"type": "Number", "value": ""}
        self.target = {"type": "Number", "value": ""}
