from module.protocol.network.message import Message


class ExchangeLeaveMessage(Message):
    def __init__(self):
        self.id = 279
