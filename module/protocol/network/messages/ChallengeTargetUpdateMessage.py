from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ChallengeTargetUpdateMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3277
        self.vars.append({"name": "challengeId", "type": "uint", "value": ""})
        self.vars.append({"name": "targetId", "type": "Number", "value": ""})
