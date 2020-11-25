from module.protocol.network.message import Message


class ExchangeAcceptMessage(Message):
    def __init__(self):
        self.id = 6022
