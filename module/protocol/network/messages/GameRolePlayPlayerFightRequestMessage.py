from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameRolePlayPlayerFightRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8916
        self.vars.append({"name": "targetId", "type": "Number", "value": ""})
        self.vars.append({"name": "targetCellId", "type": "int", "value": ""})
        self.vars.append({"name": "friendly", "type": "Boolean", "value": ""})
