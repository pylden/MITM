from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeTypesItemsExchangerDescriptionForUserMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8949
        self.objectType = {"type": "uint", "value": ""}
        self.itemTypeDescriptions = {"type": "Vector.<BidExchangerObjectInfo>", "value": ""}
