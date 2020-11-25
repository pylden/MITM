from module.protocol.network.message import Message


class ExchangeStartOkNpcShopMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 1046
        self.npcSellerId = {"type": "Number", "value": ""}
        self.tokenId = {"type": "uint", "value": ""}
        self.objectsInfos = {"type": "Vector.<ObjectItemToSellInNpcShop>", "value": ""}
