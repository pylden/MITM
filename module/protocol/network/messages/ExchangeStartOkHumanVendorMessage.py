from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeStartOkHumanVendorMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5999
        self.sellerId = {"type": "Number", "value": ""}
        self.objectsInfos = {"type": "Vector.<ObjectItemToSellInHumanVendorShop>", "value": ""}
