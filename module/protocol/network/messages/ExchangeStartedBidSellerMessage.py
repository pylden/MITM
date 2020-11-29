from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeStartedBidSellerMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6758
        self.vars.append({"name": "sellerDescriptor", "type": "SellerBuyerDescriptor", "value": ""})
        self.vars.append({"name": "objectsInfos", "type": "Vector.<ObjectItemToSellInBid>", "value": ""})
