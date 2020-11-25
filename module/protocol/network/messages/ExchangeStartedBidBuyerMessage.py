from module.protocol.network.message import Message


class ExchangeStartedBidBuyerMessage(Message):
    def __init__(self):
        self.id = 6668
