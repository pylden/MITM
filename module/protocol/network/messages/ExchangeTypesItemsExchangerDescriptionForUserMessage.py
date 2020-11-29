from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeTypesItemsExchangerDescriptionForUserMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8949
        self.vars.append({"name": "objectType", "type": "uint", "value": ""})
        self.vars.append({"name": "itemTypeDescriptions", "type": "Vector.<BidExchangerObjectInfo>", "value": ""})
