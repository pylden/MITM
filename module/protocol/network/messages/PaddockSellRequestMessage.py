from module.protocol.network.messages.NetworkMessage import NetworkMessage


class PaddockSellRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 647
        self.price = {"type": "Number", "value": ""}
        self.forSale = {"type": "Boolean", "value": ""}
