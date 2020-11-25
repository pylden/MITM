from module.protocol.network.message import Message


class ChallengeResultMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 1446
        self.challengeId = {"type": "uint", "value": ""}
        self.success = {"type": "Boolean", "value": ""}
