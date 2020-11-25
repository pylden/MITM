from module.protocol.network.message import Message


class HavenBagPackListMessage(Message):
    def __init__(self):
        self.id = 6073
