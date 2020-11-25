from module.protocol.network.message import Message


class PartyFollowStatusUpdateMessage(Message):
    def __init__(self):
        self.id = 5763
