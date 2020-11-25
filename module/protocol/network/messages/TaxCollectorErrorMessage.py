from module.protocol.network.message import Message


class TaxCollectorErrorMessage(Message):
    def __init__(self):
        self.id = 3339
