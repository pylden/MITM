from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameFightUpdateTeamMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8783
        self.vars.append({"name": "fightId", "type": "uint", "value": ""})
        self.vars.append({"name": "team", "type": "FightTeamInformations", "value": ""})
