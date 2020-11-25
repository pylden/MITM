from module.protocol.network.message import Message


class PrismsListUpdateMessage(Message):
    def __init__(self):
        self.id = 8061
