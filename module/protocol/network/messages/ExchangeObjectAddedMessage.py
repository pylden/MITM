from module.protocol.network.message import Message


class ExchangeObjectAddedMessage(Message):
    def __init__(self):
        self.id = 88
