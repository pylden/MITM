from module.protocol.network.message import Message


class ExchangeBidHouseUnsoldItemsMessage(Message):
    def __init__(self):
        self.id = 5367
