from module.protocol.network.message import Message


class SequenceNumberRequestMessage(Message):
    def __init__(self):
        self.id = 9851
