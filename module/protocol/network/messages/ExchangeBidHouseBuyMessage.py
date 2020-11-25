from module.protocol.network.message import Message


class ExchangeBidHouseBuyMessage(Message):
    def __init__(self):
        self.id = 8882
