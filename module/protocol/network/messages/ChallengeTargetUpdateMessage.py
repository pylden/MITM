from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ChallengeTargetUpdateMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3277
        self.challengeId = {"type": "uint", "value": ""}
        self.targetId = {"type": "Number", "value": ""}
