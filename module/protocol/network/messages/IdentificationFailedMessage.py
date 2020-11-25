from module.protocol.network.message import Message


class IdentificationFailedMessage(Message):
    def __init__(self):
        self.id = 5865
