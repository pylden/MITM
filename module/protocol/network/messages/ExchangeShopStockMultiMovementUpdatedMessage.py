from module.protocol.network.message import Message


class ExchangeShopStockMultiMovementUpdatedMessage(Message):
    def __init__(self):
        self.id = 6920