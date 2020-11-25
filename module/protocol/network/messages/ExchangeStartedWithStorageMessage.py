from module.protocol.network.message import Message


class ExchangeStartedWithStorageMessage(Message):
    def __init__(self):
        self.id = 8605
