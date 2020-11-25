from module.protocol.network.message import Message


class ExchangeBidPriceMessage(Message):
    def __init__(self):
        self.id = 7344
