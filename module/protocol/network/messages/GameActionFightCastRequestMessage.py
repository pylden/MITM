from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameActionFightCastRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8507
        self.spellId = {"type": "uint", "value": ""}
        self.cellId = {"type": "int", "value": ""}
