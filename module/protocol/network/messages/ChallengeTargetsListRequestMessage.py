from module.protocol.network.message import Message


class ChallengeTargetsListRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8171
        self.challengeId = {"type": "uint", "value": ""}
