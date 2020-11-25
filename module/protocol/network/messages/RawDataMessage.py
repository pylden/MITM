from module.protocol.network.message import Message


class RawDataMessage(Message):
    def __init__(self):
        self.id = 6253
