from module.protocol.network.message import Message


class ChallengeTargetUpdateMessage(Message):
    def __init__(self):
        self.id = 3277
