from module.protocol.network.message import Message


class ExchangeSellOkMessage(Message):
    def __init__(self):
        self.id = 8485
