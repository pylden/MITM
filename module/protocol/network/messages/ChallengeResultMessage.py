from module.protocol.network.message import Message


class ChallengeResultMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1446
        self.challengeId = {"type": "uint", "value": ""}
        self.success = {"type": "Boolean", "value": ""}
