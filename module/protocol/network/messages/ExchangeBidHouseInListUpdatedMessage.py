from module.protocol.network.message import Message


class ExchangeBidHouseInListUpdatedMessage(Message):
    def __init__(self):
        self.id = 5016
