from module.protocol.network.message import Message


class PartyFollowMemberRequestMessage(Message):
    def __init__(self):
        self.id = 1939
