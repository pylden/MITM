from module.protocol.network.message import Message


class ExchangeBidPriceForSellerMessage(Message):
    def __init__(self):
        self.id = 3208
