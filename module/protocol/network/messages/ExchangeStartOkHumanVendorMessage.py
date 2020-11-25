from module.protocol.network.message import Message


class ExchangeStartOkHumanVendorMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 5999
        self.sellerId = {"type": "Number", "value": ""}
        self.objectsInfos = {"type": "Vector.<ObjectItemToSellInHumanVendorShop>", "value": ""}
