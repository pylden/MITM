from module.protocol.network.message import Message


class ExchangeStartedBidSellerMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6758
        self.sellerDescriptor = {"type": "SellerBuyerDescriptor", "value": ""}
        self.objectsInfos = {"type": "Vector.<ObjectItemToSellInBid>", "value": ""}
