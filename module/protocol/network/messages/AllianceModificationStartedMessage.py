from module.protocol.network.message import Message


class AllianceModificationStartedMessage(Message):
    def __init__(self):
        self.id = 2652
