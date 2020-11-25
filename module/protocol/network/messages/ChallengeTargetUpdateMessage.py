from module.protocol.network.message import Message


class ChallengeTargetUpdateMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 3277
        self.challengeId = {"type": "uint", "value": ""}
        self.targetId = {"type": "Number", "value": ""}
