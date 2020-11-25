from module.protocol.network.message import Message


class ExchangeShopStockMovementUpdatedMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 2472
        self.objectInfo = {"type": "ObjectItemToSell", "value": ""}
