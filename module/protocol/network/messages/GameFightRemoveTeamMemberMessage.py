from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameFightRemoveTeamMemberMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6353
        self.vars.append({"name": "fightId", "type": "uint", "value": ""})
        self.vars.append({"name": "teamId", "type": "uint", "value": ""})
        self.vars.append({"name": "charId", "type": "Number", "value": ""})
