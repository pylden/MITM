from module.protocol.network.message import Message


class ExchangeBidHouseBuyResultMessage(Message):
    def __init__(self):
        self.id = 3583
