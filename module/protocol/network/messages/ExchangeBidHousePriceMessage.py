from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeBidHousePriceMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 362
        self.vars.append({"name": "genId", "type": "uint", "value": ""})
