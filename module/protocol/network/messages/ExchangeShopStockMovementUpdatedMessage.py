from module.protocol.network.message import Message


class ExchangeShopStockMovementUpdatedMessage(Message):
    def __init__(self):
        self.id = 2472
