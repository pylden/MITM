from module.protocol.network.message import Message


class ExchangeIsReadyMessage(Message):
    def __init__(self):
        self.id = 2446
