from module.protocol.network.message import Message


class EmotePlayRequestMessage(Message):
    def __init__(self):
        self.id = 9094
