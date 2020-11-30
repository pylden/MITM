from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameRolePlayPlayerFightRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8916
        self.targetId = {"type": "Number", "value": ""}
        self.targetCellId = {"type": "int", "value": ""}
        self.friendly = {"type": "Boolean", "value": ""}
