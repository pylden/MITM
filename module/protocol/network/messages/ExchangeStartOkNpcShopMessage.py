from module.protocol.network.message import Message


class ExchangeStartOkNpcShopMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1046
        self.npcSellerId = {"type": "Number", "value": ""}
        self.tokenId = {"type": "uint", "value": ""}
        self.objectsInfos = {"type": "Vector.<ObjectItemToSellInNpcShop>", "value": ""}
