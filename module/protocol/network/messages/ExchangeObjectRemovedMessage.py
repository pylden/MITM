from module.protocol.network.message import Message


class ExchangeObjectRemovedMessage(Message):
    def __init__(self):
        self.id = 1377
