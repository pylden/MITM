from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameRolePlayPlayerLifeStatusMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2514
        self.vars.append({"name": "state", "type": "uint", "value": ""})
        self.vars.append({"name": "phenixMapId", "type": "Number", "value": ""})
