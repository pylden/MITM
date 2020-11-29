from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameRolePlayArenaRegistrationStatusMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2867
        self.vars.append({"name": "registered", "type": "Boolean", "value": ""})
        self.vars.append({"name": "step", "type": "uint", "value": ""})
        self.vars.append({"name": "battleMode", "type": "uint", "value": ""})
