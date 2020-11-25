from module.protocol.network.message import Message


class ExchangeShopStockStartedMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 3010
        self.objectsInfos = {"type": "Vector.<ObjectItemToSell>", "value": ""}
