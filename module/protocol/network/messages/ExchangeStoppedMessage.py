from module.protocol.network.message import Message


class ExchangeStoppedMessage(Message):
    def __init__(self):
        self.id = 6266
