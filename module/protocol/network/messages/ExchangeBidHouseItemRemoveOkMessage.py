from module.protocol.network.message import Message


class ExchangeBidHouseItemRemoveOkMessage(Message):
    def __init__(self):
        self.id = 8207
