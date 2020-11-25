from module.protocol.network.message import Message


class ExchangeBidSearchOkMessage(Message):
    def __init__(self):
        self.id = 1977
