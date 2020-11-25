from module.protocol.network.message import Message


class ExchangeShopStockMultiMovementRemovedMessage(Message):
    def __init__(self):
        self.id = 5560
