from module.protocol.network.message import Message


class ExchangeWaitingResultMessage(Message):
    def __init__(self):
        self.id = 5686