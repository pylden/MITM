from module.protocol.network.message import Message


class ExchangeMountStableErrorMessage(Message):
    def __init__(self):
        self.id = 3820
