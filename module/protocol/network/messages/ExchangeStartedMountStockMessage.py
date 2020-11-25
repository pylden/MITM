from module.protocol.network.message import Message


class ExchangeStartedMountStockMessage(Message):
    def __init__(self):
        self.id = 6111
