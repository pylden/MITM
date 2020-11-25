from module.protocol.network.message import Message


class ChallengeTargetsListRequestMessage(Message):
    def __init__(self):
        self.id = 8171
