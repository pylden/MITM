from module.protocol.network.message import Message


class ExchangeHandleMountsMessage(Message):
    def __init__(self):
        self.id = 3008
