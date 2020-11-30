from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameActionFightCastOnTargetRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1071
        self.spellId = {"type": "uint", "value": ""}
        self.targetId = {"type": "Number", "value": ""}
