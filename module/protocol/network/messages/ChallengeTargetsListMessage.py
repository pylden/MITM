from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ChallengeTargetsListMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7959
        self.vars.append({"name": "targetIds", "type": "Vector.<Number>", "value": ""})
        self.vars.append({"name": "targetCells", "type": "Vector.<int>", "value": ""})
