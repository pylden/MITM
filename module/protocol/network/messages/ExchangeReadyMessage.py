from module.protocol.network.message import Message


class ExchangeReadyMessage(Message):
    def __init__(self):
        self.id = 4086
