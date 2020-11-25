from module.protocol.network.message import Message


class ExchangeBidHouseInListRemovedMessage(Message):
    def __init__(self):
        self.id = 6283
