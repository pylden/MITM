from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ChallengeInfoMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3983
        self.challengeId = {"type": "uint", "value": ""}
        self.targetId = {"type": "Number", "value": ""}
        self.xpBonus = {"type": "uint", "value": ""}
        self.dropBonus = {"type": "uint", "value": ""}
