from module.protocol.network.message import Message


class ExchangeStartOkHumanVendorMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 5999
        self.sellerId = {"type": "Number", "value": ""}
        self.objectsInfos = {"type": "Vector.<ObjectItemToSellInHumanVendorShop>", "value": ""}
