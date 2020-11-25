from module.protocol.network.message import Message


class ChallengeFightJoinRefusedMessage(Message):
    def __init__(self):
        self.id = 7995
