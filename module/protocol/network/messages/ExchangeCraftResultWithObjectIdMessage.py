from module.protocol.network.message import Message


class ExchangeCraftResultWithObjectIdMessage(Message):
    def __init__(self):
        self.id = 9309
