from module.protocol.network.message import Message


class ExchangeStartOkHumanVendorMessage(Message):
    def __init__(self):
        self.id = 5999
