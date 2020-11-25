from module.protocol.network.message import Message


class HouseGuildShareRequestMessage(Message):
    def __init__(self):
        self.id = 429
