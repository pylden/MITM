from module.protocol.network.message import Message


class ExchangeShopStockStartedMessage(Message):
    def __init__(self):
        self.id = 3010
