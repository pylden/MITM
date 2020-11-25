from module.protocol.network.message import Message


class IdentificationFailedBannedMessage(Message):
    def __init__(self):
        self.id = 7380
