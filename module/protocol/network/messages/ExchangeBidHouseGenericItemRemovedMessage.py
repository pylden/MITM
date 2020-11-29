from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeBidHouseGenericItemRemovedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8250
        self.vars.append({"name": "objGenericId", "type": "uint", "value": ""})
