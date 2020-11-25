from module.protocol.network.message import Message


class ExchangeStartAsVendorMessage(Message):
    def __init__(self):
        self.id = 1782
