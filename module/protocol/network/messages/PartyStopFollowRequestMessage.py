from module.protocol.network.message import Message


class PartyStopFollowRequestMessage(Message):
    def __init__(self):
        self.id = 9497
