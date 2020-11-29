from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeBidPriceMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7344
        self.vars.append({"name": "genericId", "type": "uint", "value": ""})
        self.vars.append({"name": "averagePrice", "type": "Number", "value": ""})
