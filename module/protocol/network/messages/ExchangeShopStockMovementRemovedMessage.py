from module.protocol.network.message import Message


class ExchangeShopStockMovementRemovedMessage(Message):
    def __init__(self):
        self.id = 5373
