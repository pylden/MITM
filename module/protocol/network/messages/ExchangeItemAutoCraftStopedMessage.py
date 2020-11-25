from module.protocol.network.message import Message


class ExchangeItemAutoCraftStopedMessage(Message):
    def __init__(self):
        self.id = 2052
