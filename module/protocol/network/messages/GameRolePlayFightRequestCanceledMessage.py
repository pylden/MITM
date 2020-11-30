from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameRolePlayFightRequestCanceledMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7446
        self.fightId = {"type": "uint", "value": ""}
        self.sourceId = {"type": "Number", "value": ""}
        self.targetId = {"type": "Number", "value": ""}
