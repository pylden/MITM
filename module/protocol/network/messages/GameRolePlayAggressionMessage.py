from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameRolePlayAggressionMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6136
        self.vars.append({"name": "attackerId", "type": "Number", "value": ""})
        self.vars.append({"name": "defenderId", "type": "Number", "value": ""})
