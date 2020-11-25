from module.protocol.network.message import Message


class ChallengeInfoMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 3983
        self.challengeId = {"type": "uint", "value": ""}
        self.targetId = {"type": "Number", "value": ""}
        self.xpBonus = {"type": "uint", "value": ""}
        self.dropBonus = {"type": "uint", "value": ""}
