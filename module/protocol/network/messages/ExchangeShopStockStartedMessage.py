from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeShopStockStartedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3010
        self.objectsInfos = {"type": "Vector.<ObjectItemToSell>", "value": ""}
