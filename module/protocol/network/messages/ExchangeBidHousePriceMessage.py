from module.protocol.network.message import Message


class ExchangeBidHousePriceMessage(Message):
    def __init__(self):
        self.id = 362
