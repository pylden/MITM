from module.protocol.network.message import Message


class PartyLeaveMessage(Message):
    def __init__(self):
        self.id = 2397
