from module.protocol.network.message import Message


class ExchangeStartedBidSellerMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6758
        self.sellerDescriptor = {"type": "SellerBuyerDescriptor", "value": ""}
        self.objectsInfos = {"type": "Vector.<ObjectItemToSellInBid>", "value": ""}
