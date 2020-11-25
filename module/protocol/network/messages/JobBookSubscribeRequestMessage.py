from module.protocol.network.message import Message


class JobBookSubscribeRequestMessage(Message):
    def __init__(self):
        self.id = 7697
