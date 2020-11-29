from module.protocol.network.messages.NetworkMessage import NetworkMessage


class PaddockSellRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 647
        self.vars.append({"name": "price", "type": "Number", "value": ""})
        self.vars.append({"name": "forSale", "type": "Boolean", "value": ""})
