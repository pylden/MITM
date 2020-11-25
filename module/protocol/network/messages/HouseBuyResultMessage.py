from module.protocol.network.message import Message


class HouseBuyResultMessage(Message):
    def __init__(self):
        self.id = 6050
