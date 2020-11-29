from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameFightOptionStateUpdateMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4253
        self.vars.append({"name": "fightId", "type": "uint", "value": ""})
        self.vars.append({"name": "teamId", "type": "uint", "value": ""})
        self.vars.append({"name": "option", "type": "uint", "value": ""})
        self.vars.append({"name": "state", "type": "Boolean", "value": ""})
