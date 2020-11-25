from module.protocol.network.message import Message


class ChallengeInfoMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 3983
        self.challengeId = {"type": "uint", "value": ""}
        self.targetId = {"type": "Number", "value": ""}
        self.xpBonus = {"type": "uint", "value": ""}
        self.dropBonus = {"type": "uint", "value": ""}
