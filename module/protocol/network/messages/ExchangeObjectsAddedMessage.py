from module.protocol.network.message import Message


class ExchangeObjectsAddedMessage(Message):
    def __init__(self):
        self.id = 9302
