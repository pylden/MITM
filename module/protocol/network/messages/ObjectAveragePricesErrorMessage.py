from module.protocol.network.message import Message


class ObjectAveragePricesErrorMessage(Message):
    def __init__(self):
        self.id = 3713
