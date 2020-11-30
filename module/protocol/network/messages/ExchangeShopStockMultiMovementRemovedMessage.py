from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeShopStockMultiMovementRemovedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5560
        self.objectIdList = {"type": "Vector.<uint>", "value": ""}
