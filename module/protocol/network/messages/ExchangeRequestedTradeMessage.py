from module.protocol.network.message import Message


class ExchangeRequestedTradeMessage(Message):
    def __init__(self):
        self.id = 5850
