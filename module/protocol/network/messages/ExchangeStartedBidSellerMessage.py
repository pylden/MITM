from module.protocol.network.message import Message


class ExchangeStartedBidSellerMessage(Message):
    def __init__(self):
        self.id = 6758
