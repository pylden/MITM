from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeStartedBidBuyerMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6668
        self.vars.append({"name": "buyerDescriptor", "type": "SellerBuyerDescriptor", "value": ""})
