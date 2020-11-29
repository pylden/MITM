from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameRolePlayDelayedActionFinishedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1897
        self.vars.append({"name": "delayedCharacterId", "type": "Number", "value": ""})
        self.vars.append({"name": "delayTypeId", "type": "uint", "value": ""})
