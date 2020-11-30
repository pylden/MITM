from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeBidPriceMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7344
        self.genericId = {"type": "uint", "value": ""}
        self.averagePrice = {"type": "Number", "value": ""}
