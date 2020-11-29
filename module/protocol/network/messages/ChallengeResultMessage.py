from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ChallengeResultMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1446
        self.vars.append({"name": "challengeId", "type": "uint", "value": ""})
        self.vars.append({"name": "success", "type": "Boolean", "value": ""})
