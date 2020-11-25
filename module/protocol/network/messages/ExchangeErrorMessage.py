from module.protocol.network.message import Message


class ExchangeErrorMessage(Message):
    def __init__(self):
        self.id = 3594
