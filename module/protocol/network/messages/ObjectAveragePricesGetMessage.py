from module.protocol.network.message import Message


class ObjectAveragePricesGetMessage(Message):
    def __init__(self):
        self.id = 3561
