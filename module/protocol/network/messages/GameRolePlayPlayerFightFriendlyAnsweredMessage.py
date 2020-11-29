from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameRolePlayPlayerFightFriendlyAnsweredMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1392
        self.vars.append({"name": "fightId", "type": "uint", "value": ""})
        self.vars.append({"name": "sourceId", "type": "Number", "value": ""})
        self.vars.append({"name": "targetId", "type": "Number", "value": ""})
        self.vars.append({"name": "accept", "type": "Boolean", "value": ""})
