from module.protocol.network.message import Message


class ExchangeBidHouseInListAddedMessage(Message):
    def __init__(self):
        self.id = 9210
