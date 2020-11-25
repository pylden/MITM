from module.protocol.network.message import Message


class IdentificationFailedForBadVersionMessage(Message):
    def __init__(self):
        self.id = 8091
