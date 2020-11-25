from module.protocol.network.message import Message


class ExchangeRequestedMessage(Message):
    def __init__(self):
        self.id = 8816
