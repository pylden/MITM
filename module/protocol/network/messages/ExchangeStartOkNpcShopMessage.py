from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeStartOkNpcShopMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1046
        self.vars.append({"name": "npcSellerId", "type": "Number", "value": ""})
        self.vars.append({"name": "tokenId", "type": "uint", "value": ""})
        self.vars.append({"name": "objectsInfos", "type": "Vector.<ObjectItemToSellInNpcShop>", "value": ""})
