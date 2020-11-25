from module.protocol.network.message import Message


class ExchangeShopStockMovementRemovedMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 5373
        self.objectId = {"type": "uint", "value": ""}
