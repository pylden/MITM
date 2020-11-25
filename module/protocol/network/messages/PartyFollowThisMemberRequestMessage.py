from module.protocol.network.message import Message


class PartyFollowThisMemberRequestMessage(Message):
    def __init__(self):
        self.id = 4567
