from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ChallengeInfoMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3983
        self.vars.append({"name": "challengeId", "type": "uint", "value": ""})
        self.vars.append({"name": "targetId", "type": "Number", "value": ""})
        self.vars.append({"name": "xpBonus", "type": "uint", "value": ""})
        self.vars.append({"name": "dropBonus", "type": "uint", "value": ""})
