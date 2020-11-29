from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameRolePlayDelayedActionMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4027
        self.vars.append({"name": "delayedCharacterId", "type": "Number", "value": ""})
        self.vars.append({"name": "delayTypeId", "type": "uint", "value": ""})
        self.vars.append({"name": "delayEndTime", "type": "Number", "value": ""})
