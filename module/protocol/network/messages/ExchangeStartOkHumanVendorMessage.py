from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeStartOkHumanVendorMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5999
        self.vars.append({"name": "sellerId", "type": "Number", "value": ""})
        self.vars.append({"name": "objectsInfos", "type": "Vector.<ObjectItemToSellInHumanVendorShop>", "value": ""})
