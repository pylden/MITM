from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameRolePlayArenaFightPropositionMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5355
        self.vars.append({"name": "fightId", "type": "uint", "value": ""})
        self.vars.append({"name": "alliesId", "type": "Vector.<Number>", "value": ""})
        self.vars.append({"name": "duration", "type": "uint", "value": ""})
