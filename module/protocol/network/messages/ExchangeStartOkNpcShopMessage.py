from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeStartOkNpcShopMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1046
        self.npcSellerId = {"type": "Number", "value": ""}
        self.tokenId = {"type": "uint", "value": ""}
        self.objectsInfos = {"type": "Vector.<ObjectItemToSellInNpcShop>", "value": ""}
