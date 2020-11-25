from module.protocol.network.message import Message


class ExchangeObjectsRemovedMessage(Message):
    def __init__(self):
        self.id = 5450
