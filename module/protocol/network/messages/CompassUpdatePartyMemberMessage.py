from module.protocol.network.message import Message


class CompassUpdatePartyMemberMessage(Message):
    def __init__(self):
        self.id = 7911
