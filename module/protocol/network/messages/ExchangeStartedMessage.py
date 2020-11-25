from module.protocol.network.message import Message


class ExchangeStartedMessage(Message):
    def __init__(self):
        self.id = 954
