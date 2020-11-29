from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameRolePlayPlayerFightFriendlyAnswerMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2509
        self.vars.append({"name": "fightId", "type": "uint", "value": ""})
        self.vars.append({"name": "accept", "type": "Boolean", "value": ""})
