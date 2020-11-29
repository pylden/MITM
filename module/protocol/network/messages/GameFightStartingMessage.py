from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameFightStartingMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6131
        self.vars.append({"name": "fightType", "type": "uint", "value": ""})
        self.vars.append({"name": "fightId", "type": "uint", "value": ""})
        self.vars.append({"name": "attackerId", "type": "Number", "value": ""})
        self.vars.append({"name": "defenderId", "type": "Number", "value": ""})
        self.vars.append({"name": "containsBoss", "type": "Boolean", "value": ""})
