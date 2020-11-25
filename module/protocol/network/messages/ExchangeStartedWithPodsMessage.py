from module.protocol.network.message import Message


class ExchangeStartedWithPodsMessage(Message):
    def __init__(self):
        self.id = 4599
