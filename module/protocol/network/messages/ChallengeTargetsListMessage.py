from module.protocol.network.message import Message


class ChallengeTargetsListMessage(Message):
    def __init__(self):
        self.id = 7959
