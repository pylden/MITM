from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameRolePlayDelayedActionMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4027
        self.delayedCharacterId = {"type": "Number", "value": ""}
        self.delayTypeId = {"type": "uint", "value": ""}
        self.delayEndTime = {"type": "Number", "value": ""}
